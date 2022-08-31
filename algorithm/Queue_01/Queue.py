class Queue:
    def __init__(self, n):
        self.size = n
        self.items = [None] * n
        self.front = -1
        self.rear = -1

    def enqueue(self, item):   # 큐의 뒤쪽에서 원소를 삽입하는 연산
        if self.is_full():
            print('full')       # 디버깅을 알아보기 위해 있음
        else:
            self.rear += 1
            self.items[self.rear] = item

    def dequeue(self):      # 큐의 앞쪽에서 원소를 삭제하고 반환하는 연산 (선입선출)
        if self.is_empty():
            print('empty')
        else:
            self.front += 1
            return self.items[self.front]

    def is_empty(self):     # 큐가 공백상태인지 확인하는 연산
        return self.front == self.rear

    def is_full(self):      # 큐가 포화상태인지 확인하는 연산
        return self.rear == self.size - 1

    def q_peek(self):      # 큐의 앞쪽에서 원소를 삭제 없이 반환하는 연산
        if self.is_empty():
            print("queue_empty")
        else:
            return self.items[self.front]


queue = Queue(3)  # 크기가 3인 큐 생성

print(queue.items)  # 삽입 전 큐의 모습
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.items)    # 삽입 후 큐의 모습

# 선입선출에서 세 개의 데이터를 차례로 꺼내서 출력
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue = []  # 큐 역할을 할 빈 리스트
print(queue)    # 삽입 전 큐의 모습
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)    # 삽입 후 큐의 모습

# 선입선출에서 세 개의 데이터 차례로 꺼내서 출력
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))