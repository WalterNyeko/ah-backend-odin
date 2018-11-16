from django.test import TestCase
from rest_framework.test import APIClient
import json


class BaseTest(TestCase):
    def setUp(self):
        self.client = APIClient(content_type="application/json")
        self.user_data = {
            "user": {
                "email": "johndoe@example.com",
                "username": "johndoe",
                "password": "Password123"
            }
        }

        self.user_data2 = {
            "user": {
                "email": "odin@example.com",
                "username": "odin",
                "password": "Password123"
            }
        }

        self.article_data = {
            "article": {
                "title": "some title",
                "description": "Some description",
                "body": "some story here",
                "tagList": ["mother", "love"],
                "published":"True"
            }
        }

        self.article_data2 = {
            "article": {
                "title": "some title",
                "description": "Some description needed here",
                "body": "some story here",
                "tagList": ["mother", "love"],
                "published":"True"
            }
        }

        self.report_data = {"report" : 
                                {
                                    "reason" : "this is a plagiarized article"
                                }
                            }
        self.article_like_data = {
                "article": {
		            "article_like":"True"
	            }
        }


        self.article_dislike_data = {
                "article": {
		            "article_like":"True" 
	            }
        }

        self.article_rating_data = {
            "article_rate": "4"
        }

        self.reset_token_data = {

            "email": "johndoe@example.com"
        }

        self.password_data = {

            "email": "johndoe@example.com",
            "password": "NewPassword123!"
        }


        

        self.favorite_article_data = {
            "favorite_status": "True"
        }
  
        self.report_data2 = {"report" : 
                                {
                                    "reason" : ""
                                }
                            }

        self.report_data3 = {"object" : 
                                {
                                    "reason" : "this is a plagized article"
                                }
                            }
        
        self.token = dict(self.login_user().data)['token']
        self.headers = {'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        self.slug = dict(self.create_article().data)['slug']
        


    def create_user(self):
        return self.client.post("/api/users/", self.user_data)

      
    def login_user(self):
        self.create_user()
        return self.client.post("/api/users/login/", self.user_data)
    
    def login_user2(self):
        self.create_user()
        return self.client.post("/api/users/login/", self.user_data2)

    def create_article(self):
        self.create_user()
        return self.client.post("/api/articles/", self.article_data, **self.headers)
    
    def get_article(self):
        return self.client.get("/api/articles/", self.article_data, **self.headers)
    
    def get_one_article(self):
        return self.client.get(f"/api/articles/{self.slug}", self.article_data, **self.headers)

    def delete_article(self):
        return self.client.delete(f"/api/articles/{self.slug}", self.article_data, **self.headers)
    
    def update_article(self):
        return self.client.put(f"/api/articles/{self.slug}", self.article_data, **self.headers)
    
    def bookmark_article(self):
        return self.client.post(f"/api/articles/{self.slug}/bookmark", **self.headers)
    def like_article(self):
        return self.client.post(f"/api/articles/{self.slug}/likes", self.article_like_data, **self.headers)
    
    def dislike_article(self):
        return self.client.post(f"/api/articles/{self.slug}/likes", self.article_dislike_data, **self.headers)
    
    def double_like_article(self):
        return self.client.post(f"/api/articles/{self.slug}/likes", self.article_dislike_data, **self.headers)
  
    def get_articles_with_reading_time(self):
        return self.client.get("/api/articles/readings/", self.article_data, **self.headers)
  
    def get_article_with_reading_time(self):
        return self.client.get(f"/api/articles/{self.slug}/readings/", self.article_data, **self.headers)
    
    def get_articles_with_their_reading_time(self):
        return self.client.get("/api/articles/", self.article_data, **self.headers)
    

    def create_rating(self):
        return self.client.post(f"/api/articles/{self.slug}/ratings/",self.article_rating_data, **self.headers)

    def get_one_article_rating(self):
        return self.client.get(f"/api/articles/{self.slug}/viewratings/", self.article_rating_data, **self.headers)

    def get_articles_and_their_ratings(self):
        return self.client.get(f"/api/articles/ratings/", self.article_rating_data, **self.headers)
    
    def create_token_and_send_reset_link(self):
        return self.client.post("/api/password_reset/", self.reset_token_data, **self.headers)
 
    def get_reset_token(self):
        return self.client.get("/api/reset_password/", self.reset_token_data, **self.headers)

    def reset_password(self):
        return self.client.post("/api/set_password/complete/", self.password_data, **self.headers)

    def get_articles_with_their_favorite_status(self):
        return self.client.get(f"/api/articles/{self.slug}/favorites/", self.favorite_article_data, **self.headers)
    
    def create_article_favorite(self):
        return self.client.post(f"/api/articles/{self.slug}/favorites/", self.favorite_article_data, **self.headers)
 
    def get_all_articles_with_their_favorite_status(self):
        return self.client.get(f"/api/articles/favorites/", self.favorite_article_data, **self.headers)
   
