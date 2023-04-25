# Improve query
- 같은 결과에 대한 쿼리 개수를 줄여 조회하기

## annotate
- SQL의 GROUP BY 절을 활용
- 여러 개의 쿼리문을 1개의 쿼리문으로 줄임

```python
# view.py

def function_name():
    ...
    # annotate을 사용해 첫 조회 시 댓글 개수까지 한 번에 조회
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    ...
```

## select_related
- 1:1 또는 N:1 참조 관계에서 사용
- SQL의 INNER JOIN 절을 활용

```python
# view.py

def function_name():
    ...
    # select_related를 사용해 article을 조회하면서 user까지 한 번에 조회
    articles = Article.objects.select_related('user').order_by('-pk')
    ...
```

## prefetch_related
- M:N 또는 N:1 역참조 관게에서 사용
- SQL이 아닌 Python을 이용한 JOIN이 진행됨

```python
# view.py

def function_name():
    ...
    # prefetch_related를 사용해 article을 조회하면서 comment까지 한 번에 조회
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    ...
```