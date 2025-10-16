-- Total claims per policy type
SELECT policy_type, COUNT(*) AS total_claims
FROM claims c
JOIN policies p ON c.policy_id = p.policy_id
GROUP BY policy_type;

-- Average claim processing time
SELECT AVG(DATEDIFF(end_date, start_date)) AS avg_processing_days
FROM claims;

-- Total claim amount by claim type
SELECT claim_type, SUM(claim_amount) AS total_amount
FROM claims
GROUP BY claim_type;