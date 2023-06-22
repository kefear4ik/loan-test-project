# Loan test project
Uniq list of manufacturer ids can be obtained using services.LoanService.get_contract_manufacturer_ids_with_join.
It makes only one request to database using one join operator:

'SELECT DISTINCT ON ("product"."manufacturer_id") "product"."manufacturer_id" FROM "loan_request" 
LEFT OUTER JOIN "product" ON ("loan_request"."id" = "product"."loan_request_id") WHERE "loan_request"."contract_id" = 1'

And using services.LoanService.get_contract_manufacturer_ids_with_subquery.
It makes only one request to database using subquery:
'SELECT DISTINCT "product"."manufacturer_id" FROM "product" 
WHERE "product"."loan_request_id" IN (SELECT U0."id" FROM "loan_request" U0 WHERE U0."contract_id" = 1)'