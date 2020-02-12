# Currency converter

## Usage

### Update database

Rewrite current rates:

```
POST /database
[
  {
    "currency": "USD",
    "rate": 60.012
  },
  {
    "currency": "EUR",
    "rate": 69.3
  }
]
```

Update rates with merge:

```
POST /database?merge=1
[
  {
    "currency": "USD",
    "rate": 60.012
  }
]
```

### Convert currency

```
GET /convert?from=USD&to=EUR&amount=1
```

Response:

```
{
  "amount": 0.87,
  "currency": "EUR"
}
```

