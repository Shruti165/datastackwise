import os
import django

# Set up Django environment to use models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datastackwise.settings')
django.setup()

from recommendations.models import Database

def populate_databases():
    # List of database objects with all the necessary fields
    databases = [
        {
            "name": "Amazon Redshift",
            "description": "Fully managed data warehouse for enterprise workloads.",
            "application_type": "analytics",
            "scale": "enterprise",
            "read_write_operations": "heavy_reads",
            "cost_analysis": "Pricing depends on cluster size and usage; reserved instances offer cost savings.",
            "companies_using": "Yelp, McDonald's, Lyft, Comcast.",
            "query_complexity": "complex",
            "traffic": "high",
            "geographic_distribution": "multi",
            "budget": "high",
            "compliance_needs": "high",
            "cost": "Pay for the cluster size and usage, options for reserved instances to save costs.",
            "benefits": "Columnar storage for fast queries, massively parallel processing, easy scaling.",
            "advantages": "High performance for analytics, integrates well with AWS ecosystem, automated backups.",
            "disadvantages": "Performance optimization requires expertise, can be expensive for large clusters.",
            "best_use_cases": "Data warehousing, business intelligence, large-scale analytics.",
            "data_operations": "Read-heavy analytical workloads, complex queries across large datasets.",
            "existing_teams_to_connect": "BI Teams, Data Engineering, Performance Optimization teams.",
        },
        {
            "name": "Snowflake",
            "description": "Cloud-based data warehousing service with automatic scaling.",
            "application_type": "data_warehousing",
            "scale": "enterprise",
            "read_write_operations": "heavy_reads",
            "cost_analysis": "Pricing based on compute and storage usage, can be optimized with auto-scaling.",
            "companies_using": "Netflix, Adobe, Square, Capital One.",
            "query_complexity": "complex",
            "traffic": "high",
            "geographic_distribution": "multi",
            "budget": "medium",
            "compliance_needs": "high",
            "cost": "Pay for what you use with on-demand scaling.",
            "benefits": "Separation of compute and storage, automatic scaling, supports semi-structured data.",
            "advantages": "Easy scalability, zero maintenance, optimized for diverse workloads.",
            "disadvantages": "Can become costly with large-scale data, limited control over underlying architecture.",
            "best_use_cases": "Data analytics, real-time data processing, ETL pipelines.",
            "data_operations": "Flexible queries across large datasets, supports structured and semi-structured data.",
            "existing_teams_to_connect": "Data Engineering, Data Science, BI Teams.",
        },
        {
            "name": "AWS Athena",
            "description": "Serverless, interactive query service for analyzing large-scale datasets stored in S3.",
            "application_type": "analytics",
            "scale": "small_to_medium",
            "read_write_operations": "read-heavy",
            "cost_analysis": "Pay-per-query based on the amount of data scanned.",
            "companies_using": "Spotify, Airbnb, Finra.",
            "query_complexity": "simple_to_medium",
            "traffic": "medium",
            "geographic_distribution": "multi",
            "budget": "low_to_medium",
            "compliance_needs": "medium",
            "cost": "Pricing based on the amount of data scanned per query.",
            "benefits": "No infrastructure management, query on data stored in S3, highly cost-effective for ad hoc queries.",
            "advantages": "Serverless, no infrastructure setup required, low cost for occasional queries.",
            "disadvantages": "Slower for complex queries, limited optimization compared to other services.",
            "best_use_cases": "Interactive querying of data in S3, ad-hoc analytics.",
            "data_operations": "Fast querying of large datasets stored in S3.",
            "existing_teams_to_connect": "Data Analytics, BI Teams.",
        },
        {
            "name": "AWS Glue",
            "description": "Fully managed ETL service that makes it easy to move data between data stores.",
            "application_type": "ETL_processing",
            "scale": "enterprise",
            "read_write_operations": "write-heavy",
            "cost_analysis": "Pay for the resources consumed during ETL jobs, low cost for small jobs.",
            "companies_using": "Unilever, Expedia, McKinsey.",
            "query_complexity": "medium_to_complex",
            "traffic": "medium",
            "geographic_distribution": "multi",
            "budget": "medium",
            "compliance_needs": "high",
            "cost": "Pricing based on data processing and job execution time.",
            "benefits": "Serverless, integrates with various AWS services, simplifies ETL tasks.",
            "advantages": "Automates ETL workflows, integrates well with S3, RDS, and Redshift.",
            "disadvantages": "Learning curve, requires AWS-specific knowledge, can be expensive for complex jobs.",
            "best_use_cases": "ETL jobs, data migration, data transformation tasks.",
            "data_operations": "Batch processing of data, supports custom transformations.",
            "existing_teams_to_connect": "Data Engineering, Data Science Teams.",
        },
        {
            "name": "PostgreSQL",
            "description": "Relational database known for its robustness and compliance with SQL standards.",
            "application_type": "transactional",
            "scale": "small_to_medium",
            "read_write_operations": "balanced",
            "cost_analysis": "Free, with the option for paid hosting solutions like AWS RDS.",
            "companies_using": "GitHub, Reddit, Instagram, Microsoft.",
            "query_complexity": "medium",
            "traffic": "medium_to_high",
            "geographic_distribution": "multi",
            "budget": "low_to_medium",
            "compliance_needs": "medium",
            "cost": "Free open-source, with additional cost for managed instances.",
            "benefits": "Open-source, ACID-compliant, supports complex queries.",
            "advantages": "Extensive feature set, extensibility, strong community support.",
            "disadvantages": "Requires manual scaling, slower for some types of queries compared to NoSQL.",
            "best_use_cases": "Transactional workloads, small-to-medium scale databases.",
            "data_operations": "Supports complex queries, joins, and indexing.",
            "existing_teams_to_connect": "DBAs, Data Engineering Teams.",
        },
        # Add more databases here...
    ]

    # Insert each database object into the Database model
    for db in databases:
        Database.objects.create(
            name=db["name"],
            description=db["description"],
            application_type=db["application_type"],
            scale=db["scale"],
            read_write_operations=db["read_write_operations"],
            cost_analysis=db["cost_analysis"],
            companies_using=db["companies_using"],
            query_complexity=db["query_complexity"],
            traffic=db["traffic"],
            geographic_distribution=db["geographic_distribution"],
            budget=db["budget"],
            compliance_needs=db["compliance_needs"],
            cost=db["cost"],
            benefits=db["benefits"],
            advantages=db["advantages"],
            disadvantages=db["disadvantages"],
            best_use_cases=db["best_use_cases"],
            data_operations=db["data_operations"],
            existing_teams_to_connect=db["existing_teams_to_connect"]
        )

    print("Databases populated successfully!")

# Run the populate function
if __name__ == "__main__":
    populate_databases()
