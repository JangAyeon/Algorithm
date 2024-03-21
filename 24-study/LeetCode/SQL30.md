### `1757`: Recyclable and Low Fat Products

```sql
SELECT product_id
FROM Products
WHERE low_fats="Y" AND recyclable="Y"
```

### `584`: Find Customer Referee

```sql
SELECT name
FROM Customer
WHERE referee_id!=2 OR referee_id IS NULL
```

### `595`: Big Countries

```sql
SELECT name, population, area
FROM World
WHERE area>=3000000 or population>=25000000
```

### `1148`: Article Views I

```sql
SELECT DISTINCT(author_id) as id
FROM Views
WHERE author_id = viewer_id
ORDER BY 1
```

### `1683`: Invalid Tweets

```sql
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content)>15
```
