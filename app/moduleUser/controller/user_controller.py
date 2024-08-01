from flask_openapi3 import Tag, APIBlueprint

tag = Tag(name="User", description="UserController")
UserBlueprint = APIBlueprint(
    "/user", __name__, url_prefix="/api/user", abp_tags=[tag]
)
@UserBlueprint.get('')
def get():
    print("MASUK USER")
    return "HAI USER"
