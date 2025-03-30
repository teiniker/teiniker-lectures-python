# Table Relations in SQLite


## One to One

## One to Many

In a relational database, tables are related to each other through the use
of **foreign keys**. A foreign key is a column in one table that is used to
reference a primary key in another table. The foreign key column in the
first table is called a **foreign key constraint**. The primary key column
in the second table is called a **referenced key constraint**.

The foreign key constraint is used to enforce **referential integrity**. This
means that the database will not allow a row to be inserted into the first
table if the value in the foreign key column does not match a value in the
referenced key column of the second table.

The foreign key constraint is created using the `FOREIGN KEY` clause in the
`CREATE TABLE` statement. The `FOREIGN KEY` clause specifies the name of the
foreign key column and the name of the referenced key column in the second
table.

The `FOREIGN KEY` clause can also specify the `ON DELETE` and `ON UPDATE`
actions. These actions specify what should happen to the rows in the first
table if the referenced key column in the second table is deleted or updated.

_Example:_ Get mails for user 'homer'

```sql
SELECT 
    mails.address 
FROM 
    mails
JOIN 
    users ON users.id = mails.user_id
WHERE 
    users.username = 'homer';
```

* `FROM mails`
    * The query starts from the `mails` table. 
        Initially, all mail records are selected as potential results.

* `JOIN users ON users.id = mails.user_id`
    * The query uses an inner join (`JOIN` is the same as `INNER JOIN`) 
        with the users table.
        It joins each row from `mails` to the corresponding row in `users` where:
        `users.id equals mails.user_id`

    * This establishes a link between each `mail` address and the corresponding 
        `user`'s details (like `username`, `password`).

    * After this step, each `mail` record is enriched with the information 
        of its related `user`. 

* `WHERE users.username = 'homer'`
    * This clause filters the joined result set, keeping only rows where the 
        user's `username` is exactly `'homer'`.
    * Essentially, the query now selects only those mail addresses that belong 
        to the `user` with `username` `'homer'`.
    * If there is no `user` named `'homer'`, the result set will be empty. 
        If `'homer'` exists and has no emails, the result will also be empty.

* `SELECT mails.address`
    * This clause specifies what the output should include. It only selects 
        the column address from the mails table. 
    * The final result is a list of email addresses that belong to the user `'homer'`.

```sql 
homer@springfield.com
homer@powerplant.com
```


## Many to Many
