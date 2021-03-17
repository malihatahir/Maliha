mappings = {
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "agency_name": { "type": "text" },
      "last_name": { "type": "text" },
      "first_name": { "type": "text" },
      
      "work_location_borough": { "type": "text" },
      "title_description": { "type": "text" },
      "leave_status_as_of_july_31": { "type": "text" },
      "pay_basis": { "type": "text" },
      
      "agency_start_date": { "type": "date" },
      
      "fiscal_year": { "type": "float" },
      "base_salary": { "type": "float" },
      "regular_hours": { "type": "float" },
      "regular_gross_paid": { "type": "float" },
      "ot_hours": { "type": "float" },
      "total_ot_paid": { "type": "float" },
      "total_other_pay": { "type": "float" },
    }
  }
}