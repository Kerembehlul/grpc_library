import grpc
from concurrent import futures
import time

from grpc_reflection.v1alpha import reflection
from generated import university_pb2, university_pb2_grpc

class BookService(university_pb2_grpc.BookServiceServicer):
    def ListBooks(self, request, context):
        return university_pb2.BookList(books=[
            university_pb2.Book(
                id="1",
                title="1984",
                author="George Orwell",
                isbn="9780451524935",
                publisher="Penguin",
                pageCount=328,
                stock=3
            )
        ])

    def GetBook(self, request, context):
        return university_pb2.Book(
            id=request.id,
            title="1984",
            author="George Orwell",
            isbn="9780451524935",
            publisher="Penguin",
            pageCount=328,
            stock=3
        )

    def CreateBook(self, request, context):
        return request  # mock

    def UpdateBook(self, request, context):
        return request  # mock

    def DeleteBook(self, request, context):
        return university_pb2.Empty()


# Diğer servisler için benzer yapılar eklenebilir...

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    university_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    SERVICE_NAMES = (
    university_pb2.DESCRIPTOR.services_by_name['BookService'].full_name,
    university_pb2.DESCRIPTOR.services_by_name['StudentService'].full_name,
    university_pb2.DESCRIPTOR.services_by_name['LoanService'].full_name,
    reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
