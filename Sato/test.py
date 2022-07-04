from Data import Data
i = 3
class test:
    i = 2
    def test1():
        i = 0
        print(i)
       
        def test2():
           global i 
           print(i)

        test2()
        print(i)
test.test1()