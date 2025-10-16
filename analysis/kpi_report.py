
import pandas as pd
import matplotlib.pyplot as plt

claims = pd.read_csv('../data/claims_data.csv')
claims['start_date'] = pd.to_datetime(claims['start_date'])
claims['end_date'] = pd.to_datetime(claims['end_date'])
claims['processing_days'] = (claims['end_date'] - claims['start_date']).dt.days

avg_claim_cost = claims['claim_amount'].mean()
avg_processing_time = claims['processing_days'].mean()
claim_counts = claims['claim_type'].value_counts()

print("Average Claim Cost:", avg_claim_cost)
print("Average Processing Time (days):", avg_processing_time)
print("Claim counts by type:\n", claim_counts)

claims.groupby('claim_type')['claim_amount'].sum().plot(kind='bar', title='Total Claim Amount by Type')
plt.ylabel('Amount ($)')
plt.savefig('../visuals/kpi_chart.png')
plt.show()
