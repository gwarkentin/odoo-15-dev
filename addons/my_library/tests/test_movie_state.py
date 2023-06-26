from odoo.tests.common import TransactionCase

class TestMovieState(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestMovieState, self).setUp(*args, **kwargs)
        self.test_movie = self.env['library.movie'].create({'name': 'Movie 1'})





    def test_button_available(self):
        """Make available button"""
        self.test_movie.make_available()
        self.assertEqual(self.test_movie.state, 'available',
                'Ning: Movie state should changed to available')

    #def test_button_lost(self):
    #    """Make lost button"""
    #    self.test_movie.make_lost()
    #    self.assertEqual(self.test_movie.state, 'lost',
    #            'Movie state should changed to lost')
