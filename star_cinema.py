class Star_Cinema:
    __hall_list = []

    def entry_hall(self,hall):
        Star_Cinema.__hall_list.append(Hall) 


class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.entry_hall(self)
        self.seats = {}
        self.__show_lst = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self,id,movie_name,time):
        self.__show_lst.append((id,movie_name,time))
        seat = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.seats[id] = seat
    
    def book_seats(self,id,row,col):
        self.seats[id][row][col] = 1

    def view_show_list(self):
        for show in self.__show_lst:
            print(f'id : {show[0]} movie name : {show[1]} time : {show[2]}')

    def view_available_seats(self,id):
        for i in self.seats[id]:
            print(i)
    def crct_id(self,id):
        if id in self.seats:
            return True
        else:
            return False
    def booked_seat(self,id,row,col):
        if self.seats[id][row][col]==1:
            return True
        else:
            return False
    

##input 
akatsuki = Hall(10,10,1)
akatsuki.entry_show('1','The Lord of the Rings','10.00 am')
akatsuki.entry_show('2','Interstellar','2.00 pm')


while True:
    print("1.Available Shows \n2.Available seats \n3.Book a seat \n4.Exit")
    inpt = input("enter option :")
    print('\n')

    if inpt == '1':
        print('---Available Shows---')
        akatsuki.view_show_list()
        print('\n')
    if inpt == '2':
        id = input("enter id : ")
        if akatsuki.crct_id(id) == True:
            print("available seats : ")
            akatsuki.view_available_seats(id)
        else:
            print('please enter a valid id')
    if inpt == '3':
        id = input("enter id : ")
        if akatsuki.crct_id(id) == True:
            rc = input("enter rows and colms : ")
            lst = rc.split()

            for i in range(0,len(lst)-1,2):
                row = int(lst[i])
                col = int(lst[i+1])

                if akatsuki.rows-1 >= row and akatsuki.cols-1 >= col:
                    if akatsuki.booked_seat(id,row,col) == False :
                        print(f'your seat {row} row {col} colm is booked successfully for movie id :{id}')
                        akatsuki.book_seats(id,row,col)
                    else :
                        print(f'seat {row} row {col} colm is sold out')
                else :
                    print(f'({row}{col}) are invalid rows and cols')     

        else :
            print("Invalid Id") 

    if inpt == '4':
        break          



