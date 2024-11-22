from django.db import models
from django.utils import timezone

class Database(models.Model):
    name = models.CharField(max_length=100, default='Amazon Redshift')
    description = models.TextField(default='Fully managed data warehouse for enterprise workloads.')
    application_type = models.CharField(max_length=100, default='analytics')
    scale = models.CharField(max_length=50, default='enterprise')
    read_write_operations = models.CharField(max_length=50, default='heavy_reads')
    cost_analysis = models.CharField(max_length=100, default='Pricing depends on cluster size and usage; reserved instances offer cost savings.')
    companies_using = models.TextField(default='Yelp, McDonalds, Lyft, Comcast.')
    query_complexity = models.CharField(max_length=50, default='complex')
    traffic = models.CharField(max_length=50, default='high')
    geographic_distribution = models.CharField(max_length=50, default='multi')
    budget = models.CharField(max_length=50, default='high')
    compliance_needs = models.CharField(max_length=50, default='high')
    created_at = models.DateTimeField(default=timezone.now)  # Default to the current time
    cost = models.TextField(default='Pay for the cluster size and usage, options for reserved instances to save costs.')
    benefits = models.TextField(default='Columnar storage for fast queries, massively parallel processing, easy scaling.')
    advantages = models.TextField(default='High performance for analytics, integrates well with AWS ecosystem, automated backups.')
    disadvantages = models.TextField(default='Performance optimization requires expertise, can be expensive for large clusters.')
    best_use_cases = models.TextField(default='Data warehousing, business intelligence, large-scale analytics.')
    data_operations = models.TextField(default='Read-heavy analytical workloads, complex queries across large datasets.')
    existing_teams_to_connect = models.TextField(default='BI Teams, Data Engineering, Performance Optimization teams.')

    def __str__(self):
        return self.name
