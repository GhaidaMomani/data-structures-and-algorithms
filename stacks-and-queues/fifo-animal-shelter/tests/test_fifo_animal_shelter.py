from fifo_animal_shelter.fifo_animal_shelter import Node, Queue, Animal, Cat, Dog, AnimalShelter

def test_cat():
    cat = Cat("Senan")
    assert cat.value == 'Senan'
    assert cat.type == 'cat'
    assert cat.next == None

def test_dog():
    dog = Dog("Ben")
    assert dog.value == 'Ben'
    assert dog.type == 'dog'
    assert dog.next == None


def test_shelter_enqueue():
    sh = AnimalShelter()

    sh.enqueue(Cat("1"))
    assert sh.queue1.front.value == "1"
    assert sh.queue1.rear.value == "1"
    sh.enqueue(Dog("2"))
    assert sh.queue1.rear.value == "2"
    sh.enqueue(Cat("3"))
    assert sh.queue1.rear.value == "3"
    sh.enqueue(Dog("4"))
    assert sh.queue1.rear.value == "4"
    assert sh.queue1.front.value == "1"

def test_shelter_enqueue_notcar_or_dog():
    sh = AnimalShelter()
    assert sh.enqueue(Node('1')) == "Animal must be cat or dog"

def test_shelter_dequeue():
    sh = AnimalShelter()

    sh.enqueue(Cat("1"))
    sh.enqueue(Dog("2"))
    sh.enqueue(Cat("3"))
    sh.enqueue(Cat("a"))
    sh.enqueue(Dog("4"))

    pet_adopted = sh.dequeue('cat')
    assert pet_adopted.type == 'cat'
    assert pet_adopted.value == '1'

    pet_adopted = sh.dequeue('cat')
    assert pet_adopted.type == 'cat'
    assert pet_adopted.value == '3'

