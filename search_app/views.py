# from django.shortcuts import render
# from django.http import JsonResponse
# from elasticsearch import Elasticsearch, NotFoundError
# from django.conf import settings
# import os
# import logging

# # Get Elasticsearch host from environment variables
# ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')
# ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT', '9200')

# es = Elasticsearch([f"http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"])

# def search_products(request):
#     try:
#         query = request.GET.get("q", "")
#         if not query:
#             return JsonResponse({"error": "Query parameter is required"}, status=400)
        
#         # check index is exists
#         if not es.indices.exists(index="kibana_sample_data_ecommerce"):
#             return JsonResponse({
#                 "error": "Index 'kibana_sample_data_ecommerce' does not exist. Please load sample data in Kibana.",
#                 "products": []
#             })
        
#         search_body = {
#             "query": {
#                 "match": {
#                     "products.product_name": {
#                         "query": query,
#                         "fuzziness": "AUTO"
#                     }
#                 }
#             },
#             "size": 20
#         }
        
#         response = es.search(index="kibana_sample_data_ecommerce", query=search_body["query"], size=search_body["size"])
        
#         products = []
#         for hit in response["hits"]["hits"]:
#             for product in hit["_source"].get("products", []):
#                 if query.lower() in product["product_name"].lower(): #filter only search word
#                     products.append({
#                         "product_id": product["product_id"],
#                         "product_name": product["product_name"],
#                         "price": product["price"]
#                     })
        
#         return JsonResponse({"products": products})
#     except NotFoundError:
#         logging.error(f"Index 'kibana_sample_data_ecommerce' not found")
#         return JsonResponse({
#             "error": "Index 'kibana_sample_data_ecommerce' does not exist. Please load sample data in Kibana.",
#             "products": []
#         })
#     except Exception as e:
#         logging.error(f"Search error: {str(e)}")
#         return JsonResponse({"error": str(e), "products": []}, status=500)

# def home(request):
#     return render(request, "search.html")


from django.shortcuts import render
from django.http import JsonResponse
from elasticsearch import Elasticsearch, NotFoundError
from django.conf import settings
import os
import logging

# Get Elasticsearch host from environment variables
ELASTICSEARCH_HOST = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')
ELASTICSEARCH_PORT = os.getenv('ELASTICSEARCH_PORT', '9200')

es = Elasticsearch([f"http://{ELASTICSEARCH_HOST}:{ELASTICSEARCH_PORT}"])

def search_products(request):
    try:
        query = request.GET.get("q", "").strip()
        if not query:
            return JsonResponse({"error": "Query parameter is required"}, status=400)

        # Check if index exists
        if not es.indices.exists(index="kibana_sample_data_ecommerce"):
            return JsonResponse({
                "error": "Index 'kibana_sample_data_ecommerce' does not exist. Please load sample data in Kibana.",
                "products": []
            })

        search_body = {
            "query": {
                "match": {
                    "products.product_name": {
                        "query": query,
                        "fuzziness": "AUTO"
                    }
                }
            },
            "size": 20
        }

        response = es.search(index="kibana_sample_data_ecommerce", query=search_body["query"], size=search_body["size"])

        products = []
        for hit in response["hits"]["hits"]:
            for product in hit["_source"].get("products", []):
                if query.lower() in product["product_name"].lower():  # Filter only search word
                    products.append({
                        "product_id": product["product_id"],
                        "product_name": product["product_name"],
                        "price": product["price"]
                    })

        if not products:
            return JsonResponse({"error": "This product is not listed", "products": []}, status=404)

        return JsonResponse({"products": products})
    
    except NotFoundError:
        logging.error("Index 'kibana_sample_data_ecommerce' not found")
        return JsonResponse({
            "error": "Index 'kibana_sample_data_ecommerce' does not exist. Please load sample data in Kibana.",
            "products": []
        })
    except Exception as e:
        logging.error(f"Search error: {str(e)}")
        return JsonResponse({"error": str(e), "products": []}, status=500)

def home(request):
    return render(request, "search.html")
