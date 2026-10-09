---
name: design-api
description: Designs an HTTP or library API: endpoints or functions, inputs, outputs, errors, versioning. Use before implementing a public interface.
---

## Steps
1. Define resource paths and HTTP methods. Use plural nouns (`/tasks`, `/users`). Map `GET` for retrieval, `POST` for creation, `PUT` for full updates, `PATCH` for partial updates, `DELETE` for removal.
2. Draft request and response examples. Use JSON. Example: `POST /v1/tasks` body `{"title": "fix auth"}`. Response `201 Created` with `{"id": "t_123", "status": "open"}`.
3. Specify the error model. Return standard HTTP codes. `400` for malformed input, `401` for missing auth, `403` for insufficient permissions, `404` for missing resources, `422` for validation failures, `429` for rate limits. Include `{"error": "code", "message": "string"}`.
4. Add pagination, idempotency, and versioning. Use `?page=1&limit=20` with `Link` headers. Accept an `Idempotency-Key` header on `POST` (PUT and DELETE are idempotent by definition). Prefix all paths with `/v1/`.
5. Define boundary validation. Reject unknown fields. Enforce types, formats, and ranges. Return `422` with field-level error arrays.
6. Generate the contract. Write OpenAPI 3.1 YAML or TypeScript interfaces. Validate with `swagger-cli validate` or `tsc`.

## Checklist
- [ ] Paths use plural nouns and standard HTTP methods
- [ ] Request/response examples match the contract
- [ ] Error codes follow the specified model
- [ ] Pagination, idempotency keys, and `/v1/` prefix are defined
- [ ] Validation rules cover all required fields and types
- [ ] OpenAPI spec or type signatures are complete
- [ ] No business logic leaks into the interface

## Output
- Path definitions and method mappings
- JSON request/response examples
- OpenAPI YAML or TypeScript interfaces
- Validation and error handling rules
