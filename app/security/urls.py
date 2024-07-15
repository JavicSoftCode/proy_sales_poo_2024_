from django.urls import path
from app.security.views import auth, groupModulePermissions, menus, modulos, user
from django.conf import settings
from django.conf.urls.static import static
from app.core.views.home import HomeTemplateView

app_name = "security"
urlpatterns = []

urlpatterns += [
                 path('', HomeTemplateView.as_view(), name='home'),

                 # ___________________ CREDENCIALES ADMIN  ___________________

                 # URLS de login & logout & signup & profile & changue profile & changue password
                 path('auth/login/', auth.SigninView.as_view(), name="auth_login"),
                 path('auth/logout/', auth.SignoutView.as_view(), name='auth_logout'),
                 path('auth/signup/', auth.SignupView.as_view(), name='auth_signup'),
                 path('auth/profile/', auth.ProfileView.as_view(), name='auth_profile'),
                 path('auth/update_profile/', auth.UpdateProfileView.as_view(), name='auth_update_profile'),
                 path('auth/change_password/', auth.ChangePasswordView.as_view(), name='auth_change_password'),

                 # _________________________ SEGURIDAD _________________________

                 # URLS de modulos
                 path('modules_list/', modulos.ModuleListView.as_view(), name='modules_list'),
                 path('modules_create/', modulos.ModuleCreateView.as_view(), name='modules_create'),
                 path('modules_update/<int:pk>/', modulos.ModuleUpdateView.as_view(), name='modules_update'),
                 path('modules_delete/<int:pk>/', modulos.ModuleDeleteView.as_view(), name='modules_delete'),

                 # URLS de menu
                 path('menus_list/', menus.MenuListView.as_view(), name='menus_list'),
                 path('menus_create/', menus.MenuCreateView.as_view(), name='menus_create'),
                 path('menus_update/<int:pk>/', menus.MenuUpdateView.as_view(), name='menus_update'),
                 path('menus_delete/<int:pk>/', menus.MenuDeleteView.as_view(), name='menus_delete'),

                 # URLS de grupo modulos permios
                 path('group_module_permission_list/', groupModulePermissions.GroupModulePermissionListView.as_view(),
                      name='group_module_permission_list'),
                 path('group_module_permission_add/', groupModulePermissions.GroupModulePermissionCreateView.as_view(),
                      name='group_module_permission_add'),
                 path('group_module_permission_update/<int:pk>/',
                      groupModulePermissions.GroupModulePermissionUpdateView.as_view(),
                      name='group_module_permission_update'),
                 path('group_module_permission_delete/<int:pk>/',
                      groupModulePermissions.GroupModulePermissionDeleteView.as_view(),
                      name='group_module_permission_delete'),

                 # URLS de usuarios
                 path('users_list/', user.UsersListView.as_view(), name='users_list'),
                 path('users_groups/<int:user_id>/', user.UserGroupView.as_view(), name='user_groups'),
                 path('users_delete/<int:user_id>/', user.UserDeleteView.as_view(), name='user_delete'),

               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
