## API Endpoints

### Users
- Authenticate
- CRUD
- Admin - Reader relationship: 1:N

### Books
- Admin Import books in Json format
- Reader's Reading status tracked (Not started, In progress, Finished)
- Admin Assign book to reader

### Importing book format
```json
{
    book: {
        lineno1: {'text': text, 'ill': pathtoimg},
        lineno2: {'text': text, 'ill': pathtoimg},
        lineno3: {'text': text, 'ill': pathtoimg},
        ...
    }
}
```

### Get back to original design
- No admin User
- Reader sees a catalog of story books to pick from after login
- No book is assigned but we keep track of completed and In progress books