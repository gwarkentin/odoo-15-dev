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
    
    @http.route('/books/submit_reservation', type='http', auth="user", website=True)
    def books_reservation(self, **post):
        if post.get('book_id'):
            book_id = int(post.get('book_id'))
            reservation_status = post.get('reservation_status')
            if book_id:
                book = request.env['library.book'].sudo().search([('id','=',int(book_id))])
                if book:
                    if reservation_status == 'available':
                        book.make_available()
                    if reservation_status == 'borrowed':
                        book.make_borrowed()
                    if reservation_status == 'lost':
                        book.make_lost()
                    
                    return request.redirect('/books/submit_reservation?submitted=1')

        return request.render('my_library.books_reservation_form', {
            'books': request.env['library.book'].search([]),
            'submitted': post.get('submitted', False)
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

    @http.route('/movies/submit_issues', type='http', auth="user", website=True)
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
        
        
