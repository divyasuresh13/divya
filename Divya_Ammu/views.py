from django.shortcuts import render,redirect

from django.views.generic import TemplateView,View,TemplateView,TemplateView,TemplateView,View,View,View,UpdateView,View,View,View,View
from general.models import ContactModel,FoodCategoryModel,CategoryModel,AreaModel,DeliveryPointModel,FoodOrderModel
from general.forms import ContactForm,FoodForm,CategoryForm,AreaForm,DeliveryForm,OrderForm
# Create your views here.

class HomePageVieww(TemplateView):
	template_name='index1.html'

class HomePageView(TemplateView):
	template_name='index.html'

class ContactUsView(View):
	template_name = 'contact2.html'
	form_class =ContactForm

	def get(self,request):
		form = self.form_class()
		context ={
		'conct_form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			book_cat = ContactModel.objects.create(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				contact = request.POST.get('contact'),
				message = request.POST.get('message')
				)
			return redirect('/general/contactsucess/')
		else:
			form=self.form_class()
			return render(request,self.template_name,{'form':form})

class ContactSucessView(TemplateView):
	template_name = 'contactsuccess.html'
class AboutUsView(TemplateView):
	template_name = 'about.html'

class AdminPageView(TemplateView):
	template_name = 'admin2.html'

class FoodPageView(View):
	template_name = 'food.html'
	form_class =FoodForm

	def get(self,request):
		form = self.form_class()
		context ={
		'food_form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			cat_obj = CategoryModel.objects.get(id=request.POST.get('food_category'))
			# catt_obj = AreaModel.objects.get(id=request.POST.get('area_name'))
			food = FoodCategoryModel.objects.create(
				title=request.POST.get('title'),
				# image=request.FILES.get('image'),
				description=request.POST.get('description'),
				food_category=cat_obj,
				# area_name=catt_obj,
				price = request.POST.get('price'),
				# min_quantity=request.POST.get('min_quantity')			
				)
			return redirect('/general/listfood/')
		else:
			form=self.form_class()
			return render(request,self.template_name,{'form':form})

class ListFoodView(View):
	template_name = 'food_card1.html'
	def get(self,request):
		food_list = FoodCategoryModel.objects.all()
		context = {
		'food' :food_list
		} 
		return render(request,self.template_name,context)

class FoodDetailView(View):
	template_name = 'food_detail.html'
	def get(self,request,pk):
		obj = FoodCategoryModel.objects.get(id=pk)
		context = {
		'foodd' :obj
		}
		return render(request,self.template_name,context)

class FoodDeleteView(View):
	template_name = 'food_card1.html'
	def get(self,request,pk):
		cat_obj = FoodCategoryModel.objects.get(id=pk).delete()
		food_list = FoodCategoryModel.objects.all()
		context = {
		'food' :food_list
		}
		return render(request,self.template_name,context)

class FoodUpdateView(UpdateView):
	model = FoodCategoryModel
	fields = ['title','description','food_category','price']
	template_name = 'updatefood.html'
	success_url = '/general/listfood/'

class CategoryView(View):
	template_name = 'category.html'
	form_class =CategoryForm

	def get(self,request):
		form = self.form_class()
		context ={
		'category_form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			food = CategoryModel.objects.create(
				food_category=request.POST.get('food_category'),
				)
			return redirect('/general/categorylist/')
		else:
			form=self.form_class()
			return render(request,self.template_name,{'form':form})

class ListCategoryView(View):
	template_name = 'category_list1.html'
	def get(self,request):
		cat_list = CategoryModel.objects.all()
		context = {
		'food' :cat_list
		} 
		return render(request,self.template_name,context)

class CategoryDetailView(View):
	template_name = 'category_detail.html'
	def get(self,request,pk):
		obj = CategoryModel.objects.get(id=pk)
		context = {
		'foodd' :obj
		}
		return render(request,self.template_name,context)

class CategoryDeleteView(View):
	template_name = 'category_list1.html'
	def get(self,request,pk):
		cat_obj = CategoryModel.objects.get(id=pk).delete()
		cat_list = CategoryModel.objects.all()
		context = {
		'food' :cat_list
		}
		return render(request,self.template_name,context)


class FoodAreaView(View):
	template_name = 'area.html'
	form_class =AreaForm

	def get(self,request):
		form = self.form_class()
		context ={
		'area_form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		if form.is_valid():
			food = AreaModel.objects.create(
				area_name=request.POST.get('area_name'),
				pincode=request.POST.get('pincode'),
				)
			return redirect('/general/listarea/')
		else:
			form=self.form_class()
			return render(request,self.template_name,{'form':form})

class ListAreaView(View):
	template_name = 'area_list.html'
	def get(self,request):
		areaa_list = AreaModel.objects.all()
		context = {
		'fooddd' :areaa_list
		} 
		return render(request,self.template_name,context)

class AreaUpdateView(UpdateView):
	model = AreaModel
	fields = ['area_name','pincode']
	template_name = 'update_area.html'
	success_url = '/general/listarea/'

class AreaDeleteView(View):
	template_name = 'area_list.html'
	def get(self,request,pk):
		cat_obj = AreaModel.objects.get(id=pk).delete()
		areaa_list = AreaModel.objects.all()
		context = {
		'fooddd' :areaa_list
		}
		return render(request,self.template_name,context)

class DeliveryView(View):
	template_name = 'delivery.html'
	form_class =DeliveryForm

	def get(self,request):
		form = self.form_class()
		context ={
		'delivery_form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			food = DeliveryPointModel.objects.create(
				food_name=request.POST.get('food_name'),
				food_image=request.FILES.get('food_image'),
				contact_number=request.POST.get('contact_number'),
				address=request.POST.get('address'),
				)
			return redirect('/general/listdelivery/')
		else:
			form=self.form_class()
			return render(request,self.template_name,{'form':form})


class ListDeliveryView(View):
	template_name = 'delivery_list.html'
	def get(self,request):
		del_list = DeliveryPointModel.objects.all()
		context = {
		'foood' :del_list
		} 
		return render(request,self.template_name,context)

class DeliveryUpdateView(UpdateView):
	model = DeliveryPointModel
	fields = ['food_name','food_image','contact_number','address']
	template_name = 'update_delivery.html'
	success_url = '/general/index/'


class DeliveryDeleteView(View):
	template_name = 'delivery_list.html'
	def get(self,request,pk):
		cat_obj = DeliveryPointModel.objects.get(id=pk).delete()
		del_list = DeliveryPointModel.objects.all()
		context = {
		'foood' :del_list
		}
		return render(request,self.template_name,context)

class ListDeliView(View):
	template_name = 'delivery_list.html'
	def get(self,request):
		del_list = DeliveryPointModel.objects.all()
		context = {
		'foood' :del_list
		} 
		return render(request,self.template_name,context)



class FoodOrderView(View):
	template_name = 'order.html'
	form_class =OrderForm

	def get(self,request):
		form = self.form_class()
		context ={
		'order_form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			cat_obj = CategoryModel.objects.get(id=request.POST.get('food_category'))
			catt_obj = FoodCategoryModel.objects.get(id=request.POST.get('food_name'))
			cattt_obj = AreaModel.objects.get(id=request.POST.get('area'))
			catttt_obj = DeliveryPointModel.objects.get(id=request.POST.get('address'))
			food = FoodOrderModel.objects.create(
				food_image=request.FILES.get('food_image'),
				food_category=cat_obj,
				food_name=catt_obj,
				min_quantity=request.POST.get('min_quantity'),
				available_status=request.POST.get('available_status'),
				price=request.POST.get('price'),
				area=cattt_obj,
				address=catttt_obj,
				)
			return redirect('/general/listorder/')
		else:
			form=self.form_class()
			return render(request,self.template_name,{'form':form})

class ListOrderView(View):
	template_name = 'order_list1.html'
	def get(self,request):
		ord_list = FoodOrderModel.objects.all()
		context = {
		'fudd' :ord_list
		} 
		return render(request,self.template_name,context)

class OrderUpdateView(UpdateView):
	model = FoodOrderModel
	fields = ['food_image','food_category','food_name','min_quantity','available_status','price','area','address']
	template_name = 'update_order.html'
	success_url = '/general/listorder/'

class OrderDeleteView(View):
	template_name = 'order_list1.html'
	def get(self,request,pk):
		cat_obj = FoodOrderModel.objects.get(id=pk).delete()
		ord_list = FoodOrderModel.objects.all()
		context = {
		'fudd' :ord_list
		}
		return render(request,self.template_name,context)


# class FoodVegView(View):
# 	template_name = 'veg.html'
# 	form_class =VegForm

# 	def get(self,request):
# 		form = self.form_class()
# 		context ={
# 		'veg_form':form
# 		}
# 		return render(request,self.template_name,context)

# 	def post(self,request):
# 		form = self.form_class(request.POST,request.FILES)
# 		if form.is_valid():
# 			cat_obj = CategoryModel.objects.get(id=request.POST.get('food_category'))
# 			catt_obj = FoodCategoryModel.objects.get(id=request.POST.get('food_name'))
# 			food = CategoryModel.objects.create(
# 				food_image=request.FILES.get('food_image'),
# 				food_category=cat_obj,
# 				food_name=catt_obj,
# 				min_quantity=request.POST.get('min_quantity'),
# 				available_status=request.POST.get('available_status'),
# 				price=request.POST.get('price'),
# 				)
# 			return redirect('/general/listveg/')
# 		else:
# 			form=self.form_class()
# 			return render(request,self.template_name,{'form':form})

class ListVegView(View):
	template_name = 'veg_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='veg')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'veg_list' :obj
		} 
		return render(request,self.template_name,context)

class ListNonVegView(View):
	template_name = 'non_veg_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='non veg')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'nonveg_list' :obj
		} 
		return render(request,self.template_name,context)

class ListIceCreamView(View):
	template_name = 'icecream_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='ice cream')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'ice_list' :obj
		} 
		return render(request,self.template_name,context)

class ListJuiceView(View):
	template_name = 'juice_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='juice items')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'juice_list' :obj
		} 
		return render(request,self.template_name,context)

class ListShakesView(View):
	template_name = 'shake_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='shakes')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'shake_list' :obj
		} 
		return render(request,self.template_name,context)
class ListDrinkView(View):
	template_name = 'drink_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='drinks')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'drink_list' :obj
		} 
		return render(request,self.template_name,context)

class ListChineseView(View):
	template_name = 'chinese_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='chinese dish')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'chinese_list' :obj
		} 
		return render(request,self.template_name,context)

class ListIndianView(View):
	template_name = 'indian_list.html'
	def get(self,request):
		food_obj = CategoryModel.objects.get(food_category='indian foods')
		obj=FoodOrderModel.objects.filter(food_category=food_obj)
		context = {
			'indian_list' :obj
		} 
		return render(request,self.template_name,context)

# class GalleryPageVieww(TemplateView):
# 	template_name='gallery.html'



			