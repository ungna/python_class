def add(a,b):
    return a + b

def sub(a, b):
    return a - b

PI = 3.141592

class Math:
    @staticmethod
    # staticmethod은 self를 받지않고 인스턴스를 통하지 않고 함수를 바로 호출할수있게 해줌
    def circlearea(r): # 원의 넓이
        return PI * (r ** 2)
    
    #staticmethod 안쓰면
    def circlearea2(self, r): # 원의 넓이
        return PI * (r ** 2)


# static을 안써서 객체를 생성하고 써야됨
math = Math()


# 테스트용 코드
# print(__name__)   # __main__이 나옴  호출해서 부르면 __mod2__으로 안나와서 안돌아감
if __name__ == "__main__":  # 독립적으로 실행  # 호출하면 실행안됨
    print("[mod2.py]")
    a = 10
    b = 20
    print(add(a,b))
    print(sub(a,b))

    print(f"원의 반지름 {a}, 원의 넓이{Math.circlearea(a)}")
    print(f"원의 반지름 {a}, 원의 넓이{math.circlearea(a)}")