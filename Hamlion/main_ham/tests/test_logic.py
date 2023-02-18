from django.test import TestCase
from django.urls import reverse, resolve
from main_ham.views import main
from main_ham.models import Product




class ModelTest(TestCase):

    def testProductModel(self):
        product = Product.objects.create(name = 'Liloo',price = 800,)
        self.assertEqual(str(product),'Liloo123')
        print('IsInstance :', isinstance(product,Product))
        self.assertTrue(isinstance(product,Product))
        

class UrlTest(TestCase):

    def testHomePage(self):
        url = reverse('home') # Получение name от url
        print('Resolve: ', resolve(url))
        self.assertEqual(resolve(url).func,main)

    def testCorzinePage(self):
        responce = self.client.get('/korzina/')
        print(responce)
        self.assertEqual(responce.status_code,200)


# def calculate(a,b,c,znak):
#     if znak=='+':
#         return a+b+c
#     elif znak=='-':
#         return a-b-c
#     elif znak =='*':
#         return a*b*c
#     elif znak =='/':
#         return a/b/c
#     else:
#         return 'не понимаю что делать '
#
#
# class TextExample(TestCase):
#     def test_get_sum_plus(self):
#         self.assertEqual(calculate(3,2,5,'+'),9)
#     def test_get_muptiply(self):
#         self.assertEqual(calculate(5, 3, 1, '*'), 15)
#
#     def test_get_munus(self):
#         self.assertEqual(calculate(5, 3, 1, '-'), 1)
#
#     def test_get_delen(self):
#         self.assertEqual(calculate(20, 10, 5, '/'), 0.4)


