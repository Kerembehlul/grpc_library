import grpc
from generated import university_pb2, university_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = university_pb2_grpc.BookServiceStub(channel)

    response = stub.ListBooks(university_pb2.Empty())
    for book in response.books:
        print(f"{book.title} by {book.author}")

if __name__ == '__main__':
    run()
