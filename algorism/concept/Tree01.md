### 전위 순회 

VLR 자기를 먼저 처리

```python
def preorder_traverse(T):  # 전위 순회 VLR
    if T:
        visit(T)
        preorder_traverse(T.left)
        preorder_traverse(T.right)

```

### 중위 순회

LVR 

```python
def inorder_traverse(T):  # 중위 순회 LVR
    if T:
        inorder_traverse(T.left)
        visit(T)
        inorder_traverse(T.right)

```

### 후위 순회

LRV 제일 뒤에서 부터 처리

```python
def postorder_traverse(T):  # 후위순회 LRV
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)
```

### 순회

- 시작한 부분에서 끝이 난다 

- 부모 트리로 올라가지 않는다

#### 배열을 이용한 이진 트리의 표현

- 포화 이진 트리 저장 방법

- 완전 이진 트리 저장 방법

배열을 이요한 이진 트리의 표현 (index를 이용해서 사용(0은 사용하지 않는다)) 

- 노드 번호가 i 인 노드의 부모 노드 번호   i//2

- 노드 번호가 i 인 노드의 왼쪽 자식 노드 번호 2*i

- 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 2*i +1

- 레벨 n의 노드 번호 시작 번호는 2**n

- 포화, 완전 이진 트리에서만 사용 

13까지라면 배열의 크기는 + 1을 해서 만들어 준다

- 단점 
  - 메모리 공간 낭비 발생 

#### 규칙을 따르지 않는 트리는 어떻게 할건가?

- 부모 번호를 인덱스로 자식 번호를 저장
  - 부모를 기준으로 자식들을 순회 

- 간선수 + 1 ==  정점수

```python
for i : 
```

- 자식 번호를 인덱스로 부모 번호를 저장 
  - 조상을 찾거나 루트를 찾을 때

``` python
c = 5 # c == 자식 a == 부모
while(a[c] != 0) # 루트인지 확인
	c = a[c]
    anc.append(c) # 조상목록
root = c
```

