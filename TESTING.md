# **TESTING**

You can visit the website here: [Forever Foundations](https://forever-foundations-e27644123eb0.herokuapp.com/)

# Validation

- All code was put through the CI PythonLinter, all lines have code are free of errors.


## **MANUAL TESTING**

| **MANUAL TESTING**                             |                                                          |            |
| ---------------------------------------------- | -------------------------------------------------------- | ---------- |
| **API**                                        |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| GET / Unauthenticated                          | 200 OK (welcome)                                         | Pass       |
| GET / Authenticated                            | 200 OK (welcome)                                         | Pass       |
| **LOGOUT**                                     |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| POST /dj-rest-auth/logout/ Unauthenticated     | 200 OK                                                   | Pass       |
| POST /dj-rest-auth/logout/ Authenticated       | 200 OK                                                   | Pass       |
| **COMMENT**                                    |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| GET /comments/ Unauthenticated                 | 200 OK                                                   | Pass       |
| POST /comments/ Unauthenticated                | 403 Forbidden                                            | Pass       |
| GET /comments/ Authenticated                   | 200 OK                                                   | Pass       |
| POST /comments/ Authenticated                  | 201 Created                                              | Pass       |
| DELETE /comments/<id>/ Unauthenticated         | 403 Forbidden                                            | Pass       |
| DELETE /comments/<id>/ Owner                   | 204                                                      | Pass       |
| DELETE /comments/<id>/ Not Owner               | 403 Forbidden                                            | Pass       |
| GET /comments/<id>/ Unauthenticated            | 200 OK                                                   | Pass       |
| GET /comments/<id>/ Authenticated              | 200 OK                                                   | Pass       |
| PUT /comments/<id>/ Unauthenticated            | 403 Forbidden                                            | Pass       |
| PUT /comments/<id>/ Owner                      | 200 OK                                                   | Pass       |
| PUT /comments/<id>/ Not Owner                  | 403 Forbidden                                            | Pass       |
| **POSTS**                                      |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| POST /posts/ Authenticated                     | 201 Created                                              | Pass       |
| POST /posts/ Unauthenticated                   | 403 Forbidden                                            | Pass       |
| GET /posts/ Unauthenticated                    | 200 OK                                                   | Pass       |
| GET /posts/ Authenticated                      | 200 OK                                                   | Pass       |
| DELETE /posts/<id>/ Unauthenticated            | 403 Forbidden                                            | Pass       |
| DELETE /posts/<id>/ Not Owner                  | 403 Forbidden                                            | Pass       |
| DELETE /posts/<id>/ Owner                      | 204                                                      | Pass       |
| GET /posts/<id>/ Unauthenticated               | 200 OK                                                   | Pass       |
| GET /posts/<id>/ Authenticated                 | 200 OK                                                   | Pass       |
| PUT /posts/<id>/ Owner                         | 200 OK                                                   | Pass       |
| PUT /posts/<id>/ Not Owner                     | 403 Forbidden                                            | Pass       |
| PUT /posts/<id>/ Unauthenticated               | 403 Forbidden                                            | Pass       |
| **LOVES**                                      |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| POST /likes/ Unauthenticated                   | 403 Forbidden                                            | Pass       |
| POST /likes/ Authenticated                     | 201 Created                                              | Pass       |
| GET /likes/ Authenticated                      | 200 OK                                                   | Pass       |
| GET /likes/ Unauthenticated                    | 200 OK                                                   | Pass       |
| DELETE /likes/<id>/ Unauthenticated            | 403 Forbidden                                            | Pass       |
| DELETE /likes/<id>/ Not Owner                  | 403 Forbidden                                            | Pass       |
| DELETE /likes/<id>/ Owner                      | 204                                                      | Pass       |
| GET /likes/<id>/ Authenticated                 | 200 OK                                                   | Pass       |
| GET /likes/<id>/ Unauthenticated               | 200 OK                                                   | Pass       |
| GET /liked-posts/ Unauthenticated              | 403 Forbidden                                            | Pass       |
| GET /liked-posts/ Authenticated                | 200 OK                                                   | Pass       |
| **PROFILES**                                   |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| GET /profiles/ Authenticated                   | 200 OK                                                   | Pass       |
| GET /profiles/ Unauthenticated                 | 200 OK                                                   | Pass       |
| PUT /profiles/<id>/ Unauthenticated            | 403 Forbidden                                            | Pass       |
| PUT /profiles/<id>/ Not Owner                  | 403 Forbidden                                            | Pass       |
| PUT /profiles/<id>/ Owner                      | 200 OK                                                   | Pass       |
| GET /profiles/<id>/ Authenticated              | 200 OK                                                   | Pass       |
| GET /profiles/<id>/ Unauthenticated            | 200 OK                                                   | Pass       |
| **FOLLOWERS**                                  |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| POST /followers/ Unauthenticated               | 403 Forbidden                                            | Pass       |
| POST /followers/ Authenticated                 | 201 Created                                              | Pass       |
| GET /followers/ Authenticated                  | 200 OK                                                   | Pass       |
| GET /followers/ Unauthenticated                | 200 OK                                                   | Pass       |
| DELETE /followers/<id>/ Unauthenticated        | 403 Forbidden                                            | Pass       |
| DELETE /followers/<id>/ Not Owner              | 403 Forbidden                                            | Pass       |
| DELETE /followers/<id>/ Owner                  | 204                                                      | Pass       |
| GET /followers/<id>/ Authenticated             | 200 OK                                                   | Pass       |
| GET /followers/<id>/ Unauthenticated           | 200 OK                                                   | Pass       |
| GET /followed-posts/ Unauthenticated           | 403 Forbidden                                            | Pass       |
| GET /followed-posts/ Authenticated             | 200 OK                                                   | Pass       |
| **REVIEWS**                                    |                                                          |            |
| **Test**                                       | **Expected**                                             | **Result** |
| GET /reviews/ Unauthenticated                  | 200 OK                                                   | Pass       |
| POST /reviews/ Unauthenticated                 | 403 Forbidden                                            | Pass       |
| GET /reviews/ Authenticated                    | 200 OK                                                   | Pass       |
| POST /reviews/ Authenticated                   | 201 Created                                              | Pass       |
| DELETE /reviews/<id>/ Unauthenticated          | 403 Forbidden                                            | Pass       |
| DELETE /reviews/<id>/ Owner                    | 204                                                      | Pass       |
| DELETE /reviews/<id>/ Not Owner                | 403 Forbidden                                            | Pass       |
| GET /reviews/<id>/ Unauthenticated             | 200 OK                                                   | Pass       |
| GET /reviews/<id>/ Authenticated               | 200 OK                                                   | Pass       |
| PUT /reviews/<id>/ Unauthenticated             | 403 Forbidden                                            | Pass       |
| PUT /reviews/<id>/ Owner                       | 200 OK                                                   | Pass       |
| PUT /reviews/<id>/ Not Owner                   | 403 Forbidden                                            | Pass       |