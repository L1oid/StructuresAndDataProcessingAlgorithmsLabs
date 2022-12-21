class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def insertLeftChild(self, newNode):
        self.leftChild = newNode

    def insertRightChild(self, newNode):
        self.rightChild = newNode

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


class Game:
    def __init__(self):
        START_POS = [
            'Это млекопитающее?',
            # left
            [
                'Оно лает?',
                # left
                ['Собака', [], []],
                # right
                ['Кошка', [], []]
            ],
            # right
            [
                'Оно покрыто чушуей?',
                # left
                [
                    'Оно дышит в воде?',
                    # left
                    ['Рыба', [], []],
                    # right
                    ['Змея', [], []]
                ],
                # right
                ['Птица', [], []]
            ]
        ]

        self.tree = self._init_game(START_POS)

    def _init_game(self, start_pos) -> BinaryTree:
        ans, left, right = start_pos
        bt = BinaryTree(ans)

        if len(left) > 0:
            bt.insertLeftChild(self._init_game(left))
        if len(right) > 0:
            bt.insertRightChild(self._init_game(right))

        return bt

    def play(self):
        print('Игра "Животные"! Вы загадываете животное, а я пытаюсь отгадать по средству вопросов!')

        while True:
            ans = str(input('Начать игру? (да/нет)\n')).lower()

            if ans == 'да':
                self._play()
            elif ans == 'нет':
                break
            else:
                print('Ошибка! Введите ваш ответ еще раз!')

    def _play(self):
        current_tree = self.tree

        while True:
            if current_tree.getLeftChild() is None:
                print('Ответ: ' + current_tree.key)
                ret = self._verify_ans()

                if ret is not None:
                    n_ans, n_anim = ret
                    c_anim = current_tree.key
                    current_tree.key = n_ans
                    current_tree.insertLeft(n_anim)
                    current_tree.insertRight(c_anim)
                break

            ans = str(input(current_tree.key + ' (да/нет)\n')).lower()
            if ans == 'да':
                current_tree = current_tree.getLeftChild()
            elif ans == 'нет':
                current_tree = current_tree.getRightChild()
            else:
                print('Ошибка! Введите ваш ответ еще раз!')

    def _verify_ans(self):
        while True:
            ans = str(input('Я угадала? (да/нет)\n')).lower()
            if ans == 'да':
                return None
            elif ans == 'нет':
                n_ans = str(input('Напишите уточняющий вопрос: '))
                n_anim = str(input('Напишите загаданное вами животное: '))
                return n_ans, n_anim
            else:
                print('Ошибка! Введите ваш ответ еще раз!')


game = Game()
game.play()
