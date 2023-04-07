import strawberry
from strawberry import auto
from strawberry.types import Info

import typing
from django.conf import settings

from . import models
from users.types import UserType
from reviews.types import ReviewType
from wishlists.models import Wishlist


@strawberry.django.type(models.Room)
class RoomType:
    id: auto
    name: auto
    kind: auto
    owner: "UserType"

    @strawberry.field
    def reviews(self, page: typing.Optional[int] = 1) -> typing.List["ReviewType"]:
        page_size = 3
        start = (page - 1) * page_size
        end = start + page_size
        return self.reviews.all()[start:end]

    @strawberry.field
    def rating(self) -> str:
        return self.rating()
    
    @strawberry.field
    def is_owner(self, info:Info) -> bool:
        return self.owner == info.context.request.user
    
    @strawberry.field
    def is_liked(self, info:Info) -> bool:
        return Wishlist.objects.filter(
            user=info.context.request.user,
            rooms__pk=self.pk,
        ).exists()
