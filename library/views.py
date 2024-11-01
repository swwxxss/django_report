from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Order
from .forms import BookForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_to_cart(request, book_id):
    # Отримуємо книгу за ID
    book = get_object_or_404(Book, id=book_id)

    # Додаємо книгу до кошика в сесії
    if 'cart' not in request.session:
        request.session['cart'] = []

    request.session['cart'].append(book.id)
    request.session.modified = True  # Вказуємо, що сесія була змінена

    return redirect('cart_view')


@login_required
def profile_view(request):
    user = request.user
    return render(request, 'library/profile.html', {'user': user})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')

        # Перевірка наявності імені користувача
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Це ім\'я користувача вже використовується!')
            return render(request, 'library/register.html')

        # Перевірка наявності електронної пошти
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Ця електронна пошта вже використовується!')
            return render(request, 'library/register.html')

        # Створення нового користувача
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()
            messages.success(request, 'Реєстрація успішна!')
            return redirect('login')  # Перенаправлення на сторінку входу після успішної реєстрації
        except Exception as e:
            messages.error(request, f'Помилка: {str(e)}')

    return render(request, 'library/register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        # Перевірка на пусті поля
        if not username or not password:
            messages.error(request, "Будь ласка, заповніть всі поля.")
            return render(request, 'library/login.html')

        # Автентифікація користувача
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Ви увійшли успішно!")
            return redirect('library/home')
        else:
            messages.error(request, "Неправильні дані для входу")

    return render(request, 'profile_view')




@login_required
def user_profile(request):
    user = request.user
    profile = user.userprofile

    context = {
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'username': profile.username,
        'email': profile.email,
    }

    return render(request, 'your_template.html', context)


@login_required
def admin_profile(request):
    admin = request.user

    # Перевірка, чи є користувач адміністратором
    if admin.username == 'admin' and admin.userprofile.password == 'admin':
        # Перенаправлення на book_list.html
        return redirect('book_list')  # Використання імені маршруту для перенаправлення

    # Якщо користувач не адміністратор, не робимо нічого (або можете просто не повертати нічого)
    return




@login_required
def your_view(request):
    if request.user.groups.filter(name='Admins').exists():
        # Логіка для адміністраторів
        pass
    elif request.user.groups.filter(name='Normal Users').exists():
        pass
    else:
        pass


def profile(request):
    return render(request, 'profile.html')


def home(request):
    books = Book.objects.all()  # Отримати всі книги з бази даних
    return render(request, 'library/home.html', {'books': books})



def search_books(request):
    query = request.GET.get('query')
    if query:
        books = Book.objects.filter(book_name__icontains=query)  # Пошук за назвою книги
    else:
        books = Book.objects.none()  # Якщо запит пустий, нічого не повертаємо

    return render(request, 'library/search_results.html', {'books': books, 'query': query})


def add_to_cart(request, book_id):
    # Отримуємо книгу за її ідентифікатором
    book = get_object_or_404(Book, id=book_id)

    # Ініціалізуємо кошик у сесії, якщо його ще немає
    cart = request.session.get('cart', [])

    # Додаємо книгу до кошика, якщо її ще там немає
    if book_id not in cart:
        cart.append(book_id)  # додаємо book_id до кошика
        request.session['cart'] = cart  # оновлюємо кошик у сесії
        messages.success(request, f'{book.book_name} додано до кошика!')
    else:
        messages.info(request, f'{book.book_name} вже у кошику.')

    # Перенаправляємо на сторінку з інформацією про книгу
    return render(request, 'library/book_information.html', {'book': book})


def remove_from_cart(request, book_id):
    # Ініціалізуємо кошик у сесії
    cart = request.session.get('cart', [])

    # Видаляємо книгу з кошика, якщо вона там є
    if book_id in cart:
        cart.remove(book_id)
        request.session['cart'] = cart
        messages.success(request, 'Книгу видалено з кошика.')
    else:
        messages.info(request, 'Книга не знайдена в кошику.')

    # Перенаправляємо назад до кошика
    return redirect('cart_view')


def cart_view(request):
    # Отримати кошик із сесії
    cart = request.session.get('cart', [])

    # Отримати всі книги, які є в кошику
    books_in_cart = Book.objects.filter(id__in=cart)

    return render(request, 'library/cart.html', {'books': books_in_cart})



def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'library/book_detail.html', {'book': book})




def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def product_list(request):
    books = Book.objects.all()
    return render(request, 'path_to_your_template.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)  # Додайте request.FILES
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'library/book_confirm_delete.html', {'book': book})


@login_required
def add_to_cart(request, book_id):
    # Отримуємо книгу за ID
    book = get_object_or_404(Book, id=book_id)

    # Додаємо книгу до кошика в сесії
    cart = request.session.get('cart', [])

    # Додаємо книгу до кошика, якщо її там немає
    if book.id not in cart:
        cart.append(book.id)
        request.session['cart'] = cart
        messages.success(request, f'{book.book_name} додано до кошика!')
    else:
        messages.info(request, f'{book.book_name} вже у кошику.')

    # Перенаправляємо на сторінку з інформацією про книгу
    return render(request, 'library/book_information.html', {'book': book})


def checkout(request):
    cart = request.session.get('cart', [])
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Створюємо новий об'єкт замовлення
        order = Order(
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            email=email,
        )
        order.save()  # Зберігаємо замовлення у базі даних

        # Додаємо книги до замовлення
        for book_id in cart:
            book = get_object_or_404(Book, id=book_id)
            order.books.add(book)  # Додаємо книгу до замовлення

        # Очищення кошика
        request.session['cart'] = []  # Очистіть кошик після оформлення замовлення

        messages.success(request, "Ваше замовлення оформлено успішно!")
        return redirect('order_success')

    return render(request, 'library/checkout.html', {'cart': cart})

def order_success(request):
    return render(request, 'library/order_success.html')

def process_order(request):
    if request.method == 'POST':
        # Логіка обробки замовлення
        # Ваш код для обробки замовлення (збереження в базі даних, надсилання електронної пошти тощо)

        # Очистити кошик
        if 'books' in request.session:
            del request.session['books']  # видаляємо всі товари з кошика

        return redirect('success')  # перенаправлення на сторінку успіху
    return render(request, 'library/checkout.html')