from queue import Queue

if __name__ == '__main__':
    quwu = Queue()
    print(quwu.isEmpty())
    quwu.enqueue(2)
    quwu.enqueue("Hello")
    print(quwu.__str__())
    print(quwu.size())
    print(quwu.isEmpty())
    print(quwu.front().data)
    quwu.dequeue()
    quwu.dequeue()
    print(quwu.isEmpty())
