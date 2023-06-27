# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/books', type='http', auth="user", website=True)
    def library_books(self):
        return request.render(
            'my_library.books', {
                'books': request.env['library.book'].search([]),
            })

    @http.route('/books/<model("library.book"):book>', type='http', auth="user", website=True)
    def library_book_detail(self, book):
        return request.render(
            'my_library.book_detail', {
                'book': book,
            })

    @http.route('/books/submit_issues', type='http', auth="user", website=True)
    def books_issues(self, **post):
        if post.get('book_id'):
            book_id = int(post.get('book_id'))
            issue_description = post.get('issue_description')
            request.env['book.issue'].sudo().create({
                'book_id': book_id,
                'issue_description': issue_description,
                'submitted_by': request.env.user.id
            })
            return request.redirect('/books/submit_issues?submitted=1')

        return request.render('my_library.books_issue_form', {
            'books': request.env['library.book'].search([]),
            'submitted': post.get('submitted', False)
        })
    
    @http.route('/books/submit_reservation', type='http', auth="user", website=True, methods=['POST',])
    def books_reservation_post(self, **post):
        error = ''
        if post.get('book_id'):
            book_id = int(post.get('book_id'))
            reservation_status = post.get('reservation_status')
            if book_id:
                books = request.env['library.book'].sudo().search([('id','=',book_id)])
                if len(books) > 0:
                    if reservation_status == 'available':
                        books[0].make_available()
                        if books[0].state != 'available':
                            error = f'unable to change from {books[0].state} to "available"'
                    if reservation_status == 'borrowed':
                        books[0].make_borrowed()
                        if books[0].state != 'borrowed':
                            error = f'unable to change from {books[0].state} to "borrowed"'
                    if reservation_status == 'lost':
                        books[0].make_lost()
                        if books[0].state != 'lost':
                            error = f'unable to change from {books[0].state} to "lost"'
                    books[0].write({'state':books[0].state})
                    if not error:
                        return request.redirect(f'/books/submit_reservation?submitted=1&book_id={book_id}')

        books = request.env['library.book'].search([])
        if post.get('book_id'):
            book_id = int(post.get('book_id'))
            if book_id:
                books = request.env['library.book'].sudo().search([('id','=',book_id)])

        return request.render('my_library.books_reservation_form', {
            'books': books,
            'submitted': post.get('submitted', False),
            'error': error,
            'book_id': int(post.get('book_id'))
        })
        
    @http.route('/books/submit_reservation', type='http', auth="user", website=True, methods=['GET',])
    def books_reservation_gets(self, **post):
        books = request.env['library.book'].search([])
        if post.get('book_id'):
            book_id = int(post.get('book_id'))
            if book_id:
                books = request.env['library.book'].sudo().search([('id','=',book_id)])
        return request.render('my_library.books_reservation_form', {
            'books': books,
            'submitted': post.get('submitted', False),
        })
           
         
    @http.route('/movies', type='http', auth="user", website=True)
    def library_movies(self):
        return request.render(
            'my_library.movies', {
                'movies': request.env['library.movie'].search([]),
            })

    @http.route('/movies/<model("library.movie"):movie>', type='http', auth="user", website=True)
    def library_movie_detail(self, movie):
        return request.render(
            'my_library.movie_detail', {
                'movie': movie,
            })

    @http.route('/movies/submit_reservation', type='http', auth="user", website=True)
    def movies_issues(self, **post):
        if post.get('movie_id'):
            movie_id = int(post.get('movie_id'))
            issue_description = post.get('issue_description')
            request.env['movie.issue'].sudo().create({
                'movie_id': movie_id,
                'issue_description': issue_description,
                'submitted_by': request.env.user.id
            })
            return request.redirect('/movies/submit_issues?submitted=1')

        return request.render('my_library.movies_issue_form', {
            'movies': request.env['library.movie'].search([]),
            'submitted': post.get('submitted', False)
        })
        
        
