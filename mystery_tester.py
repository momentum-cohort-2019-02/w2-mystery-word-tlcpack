from mw_tester import is_letter, correct_length, in_current_guesses

# how to write tests when functions don't take parameters?

def test_is_letter():
    assert is_letter('a')
    assert is_letter('K')
    assert not is_letter('9')
    assert not is_letter('ls')
    assert is_letter('e')

def test_correct_length():
    assert correct_length('d')
    assert correct_length('F')
    assert not correct_length('df')
    assert not correct_length('KL')
    assert not correct_length('')

def test_in_current_guesses():
    assert in_current_guesses('a')
    assert in_current_guesses('b')
    assert not in_current_guesses('n')
    assert not in_current_guesses('9')
    assert in_current_guesses('C')
    assert not in_current_guesses('V')