
# generate pb2
python -m grpc_tools.protoc -I. --python_out=../python/ --grpc_python_out=../python/ ./helloworld.proto