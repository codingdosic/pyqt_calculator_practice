import sys
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        subMain_layout = QHBoxLayout()
        
        layout_newFunc = QVBoxLayout()
        layout_number = QGridLayout()
        layout_clear_equal = QGridLayout()

        layout_operation = QGridLayout()
        
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        # label_equation = QLabel("Equation: ") # 삭제
        # label_solution = QLabel("Solution: ") # 삭제
        self.equation = QLineEdit("")
        # self.solution = QLineEdit("") # 삭제

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_equation_solution.addRow(self.equation) # label_equation 삭제
        #layout_equation_solution.addRow(label_solution, self.solution) # 삭제

        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        button_backspace = QPushButton("Backspace")
        button_equal = QPushButton("=")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)


        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_operation.addWidget(button_backspace, 0, 0)
        layout_operation.addWidget(button_division, 1, 0)
        layout_operation.addWidget(button_product, 2, 0)
        layout_operation.addWidget(button_minus, 3, 0)
        layout_operation.addWidget(button_plus, 4, 0)
        layout_operation.addWidget(button_equal, 5, 0)
        

        ### =, clear, backspace 버튼 생성
        button_mod = QPushButton("%")
        button_clear_CE = QPushButton("CE")
        button_clear_C = QPushButton("C")
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_square_root = QPushButton("√x")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        
        button_clear_C.clicked.connect(self.button_clear_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_clear_equal.addWidget(button_mod, 0, 0)
        layout_clear_equal.addWidget(button_clear_CE, 0, 1)
        layout_clear_equal.addWidget(button_clear_C, 0, 2)
        layout_clear_equal.addWidget(button_inverse, 1, 0)
        layout_clear_equal.addWidget(button_square, 1, 1)
        layout_clear_equal.addWidget(button_square_root, 1, 2)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                if x == 2: x -= 2
                elif x == 0: x += 2
                layout_number.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_number.addWidget(button_double_zero, 3, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        layout_newFunc.addLayout(layout_clear_equal)
        layout_newFunc.addLayout(layout_number)

        subMain_layout.addLayout(layout_newFunc)
        subMain_layout.addLayout(layout_operation)

        main_layout.addLayout(layout_equation_solution)

        main_layout.addLayout(subMain_layout)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        self.equation.setText(str(eval(equation)))

    def button_clear_clicked(self):
        self.equation.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())