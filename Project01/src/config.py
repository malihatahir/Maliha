mappings = {
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "plate": { "type": "keyword" },
      "state": { "type": "keyword" },
      "license_type": { "type": "keyword" },
      
      "summons_number": { "type": "float" },
      
      "issue_date": { "type": "date", "format": "mm/dd/yyyy" },
      "violation": { "type": "keyword" },
      "judgement_entry_date": { "type": "date", "format": "mm/dd/yyyy" },
      "fine_amount": { "type": "float" },
      
      "penalty_amount": { "type": "float" },
      
      "interest_amount": { "type": "float" },
      "reduction_amount": { "type": "float" },
      "payment_amount": { "type": "float" },
      "amount_due": { "type": "float" },
      "precinct": { "type": "keyword" },
      "county": { "type": "keyword" },
      "issuing_agency": { "type": "keyword" }
    }
  }
}