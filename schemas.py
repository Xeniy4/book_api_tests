schema_auth_user = {
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


schema_create_book = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "bookingid": {
      "type": "integer"
    },
    "booking": {
      "type": "object",
      "properties": {
        "firstname": {
          "type": "string"
        },
        "lastname": {
          "type": "string"
        },
        "totalprice": {
          "type": "integer"
        },
        "depositpaid": {
          "type": "boolean"
        },
        "bookingdates": {
          "type": "object",
          "properties": {
            "checkin": {
              "type": "string"
            },
            "checkout": {
              "type": "string"
            }
          },
          "required": [
            "checkin",
            "checkout"
          ]
        },
        "additionalneeds": {
          "type": "string"
        }
      },
      "required": [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
        "additionalneeds"
      ]
    }
  },
  "required": [
    "bookingid",
    "booking"
  ]
}

schema_get_book = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "firstname": {
      "type": "string"
    },
    "lastname": {
      "type": "string"
    },
    "totalprice": {
      "type": "integer"
    },
    "depositpaid": {
      "type": "boolean"
    },
    "bookingdates": {
      "type": "object",
      "properties": {
        "checkin": {
          "type": "string"
        },
        "checkout": {
          "type": "string"
        }
      },
      "required": [
        "checkin",
        "checkout"
      ]
    }
  },
  "required": [
    "firstname",
    "lastname",
    "totalprice",
    "depositpaid",
    "bookingdates"
  ]
}