
PRODUCTS_PATH=./proto/products/products.proto
PRODUCTS_OUTPUT=gen/products

AUTH_PATH=./proto/authorization/authorization.proto
AUTH_OUTPUT=gen/authorization

IMAGES_PATH=./proto/products/images.proto
IMAGES_OUTPUT=gen/images

PROTOC_GEN_GENERIC=python -m grpc_tools.protoc

PROTOC_PRODUCTS=$(PROTOC_GEN_GENERIC) -I$(PRODUCTS_OUTPUT)=proto/products --python_out=. --grpc_python_out=. $(PRODUCTS_PATH)
PROTOC_AUTH=$(PROTOC_GEN_GENERIC) -I$(AUTH_OUTPUT)=proto/authorization --python_out=. --grpc_python_out=. $(AUTH_PATH)
PROTOC_IMAGES=$(PROTOC_GEN_GENERIC) -I$(IMAGES_OUTPUT)=proto/products --python_out=. --grpc_python_out=. $(IMAGES_PATH)

all: products auth images

products:
	$(PROTOC_PRODUCTS)

auth:
	$(PROTOC_AUTH)

images:
	$(PROTOC_IMAGES)
