auth_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "session_jwt": {
      "type": "string"
    },
    "action": {
      "type": "string"
    }
  },
  "required": [
    "session_jwt",
    "action"
  ]
}