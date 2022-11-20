from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import permissions
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
import requests
import json
from rest_framework.response import Response
from collections import Counter


class viewPosts(APIView):

    def get(self, request):

        posts_response = requests.get(
            'https://jsonplaceholder.typicode.com/posts')
        posts_data = json.loads(posts_response.text)
        # del posts_data['userId']
        # print(posts.text)

        comments_response = requests.get(
            'https://jsonplaceholder.typicode.com/comments')
        comments_data = json.loads(comments_response.text)
        # comments_data == response.json()

        # count the comments
        counts = Counter([d['postId'] for d in comments_data])

        # add the counts to each post
        for d in posts_data:
            d["number of comments"] = counts[d['id']]
            d.pop("userId", None)
        # posts_data[5]['number of comments'] = 60
        # print(posts_data[5]['number of comments'])

        # sort posts by number of comments in descending order
        posts_data.sort(
            key=lambda x: x['number of comments'], reverse=True)

        # print(posts_data)
        return Response(posts_data)


class viewPostDetails(APIView):

    def get(self, request, input):
        posts_response = requests.get(
            'https://jsonplaceholder.typicode.com/posts')
        # queryset = posts_response
        posts_data = json.loads(posts_response.text)

        comments_response = requests.get(
            'https://jsonplaceholder.typicode.com/comments')
        comments_data = json.loads(comments_response.text)
        # comments_data == response.json()

        # count the comments
        counts = Counter([d['postId'] for d in comments_data])

        # add the counts to each post
        # input = self.kwargs['keyword']
        for d in posts_data:
            d["number of comments"] = counts[d['id']]
            d.pop("userId", None)
        # posts_data[5]['number of comments'] = 60
        # print(posts_data[5]['number of comments'])

        # sort posts by number of comments in descending order
        posts_data.sort(
            key=lambda x: x['number of comments'], reverse=True)

        output = {}
        for field in posts_data:
            if input == field['id']:
                # print(field['id'])
                output = field

            # elif input == field['userId']:
            #     # print(field['userId'])
            #     output = field

            else:
                input = "{input}"
                if input == field['title']:
                    output = field
                    print(field['title'])
                else:
                    print('none')
            #     for key in field.keys():
            #         if all(x in key for x in input):
            #             print(key)

            return Response(output)
