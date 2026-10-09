---
name: containers-and-deploy
description: Packages and deploys services with containers. Use for Dockerfiles, compose, Kubernetes or a server deploy.
---

## Steps
1. Build a small image. Use a multi-stage `Dockerfile`. Pin the base tag (e.g., `python:3.12-slim@sha256:...`). Copy only the files needed at run time. Set `USER app` before the final `CMD`.
2. Inject config and secrets. Pass runtime config via `ENV` or `--env-file`. Store credentials in a secret store (e.g., `docker secret`, `kubectl create secret`, or AWS Secrets Manager). Never write keys to the image.
3. Add health checks and shutdown handling. Define a `HEALTHCHECK` that calls the app's health endpoint (the image must contain the tool it uses, for example `curl`). Catch `SIGTERM` in the app, flush buffers, and close connections before exiting.
4. Apply resource limits. Set `deploy.resources.limits` in `docker-compose.yml` or Kubernetes manifests. Cap CPU and memory. Add `reservations` to guarantee baseline capacity.
5. Write a rollback plan. Tag the current running image as `stable`. Keep the previous two versions. If the new deployment fails health checks or spikes errors, revert the service to `stable` immediately.

## Checklist
- [ ] Base image tag is pinned and verified.
- [ ] Container runs as a non-root user.
- [ ] Secrets reference a secure store, not plaintext.
- [ ] Health check endpoint exists and matches the Dockerfile directive.
- [ ] Resource limits are defined for CPU and memory.
- [ ] Rollback procedure is documented and executable.
- [ ] Graceful shutdown handler is implemented and tested.

## Output
- Updated `Dockerfile` and deployment manifests (`docker-compose.yml` or Kubernetes YAML).
- Rollback runbook with exact revert commands.
- Environment variable template and secret injection instructions.
