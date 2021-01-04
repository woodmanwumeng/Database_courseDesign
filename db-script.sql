create table Reader(
    ReaderID int,
    ReaderName varchar(10) default '张三',
    Sex varchar(1),
    Age int default 18,
    TEL varchar(12) default NULL,
    primary key (ReaderID),
    unique (ReaderID),
    CHECK ( Sex='男' or Sex='女')
);

create table Book(
  ISBN varchar(20),
  BookName varchar(20) not null ,
  Author varchar(20) default ' ',
  Price int ,
    primary key (ISBN),
    unique (ISBN),
    check ( Price>0 )
);

create table CollectionOfBook(
    ISBN varchar(20),
    TotalNum int default 0,
    foreign key (ISBN)
        references Book(ISBN)
);
alter table collectionofbook add constraint check(TotalNum>=0);

CREATE table Employee(
    EmployeeID int primary key ,
    EmployName varchar(20),
    EmploySex varchar(1),
    EmployAge int,
    EmployTEL varchar(20),
    Salary int,
    check ( EmploySex ='男' or EmploySex = '女')
);
//创建触发器
create trigger increaseNumberOfBooks after insert on purchasebook
    for each row
    begin
        if not exists(select 1 from collectionofbook where NEW.ISBN in(select ISBN from collectionofbook)) then
            begin
       insert into CollectionOfBook(ISBN, TotalNum) VALUE (NEW.ISBN,NEW.PurchaseNum);
            end;
        else
            begin
                update CollectionOfBook set TotalNum = TotalNum+NEW.PurchaseNum
        where CollectionOfBook.ISBN = NEW.ISBN;
                end;
        end if;
    end;

create trigger decreaseNumberOfBooks after insert on sell
    for each row
    begin
        update CollectionOfBook set TotalNum = TotalNum-NEW.AlreadySold
        where  CollectionOfBook.ISBN = NEW.ISBN;
    end;

create  trigger borrowBook before insert on borrow
    for each row
    begin
        if (select TotalNum from collectionofbook where CollectionOfBook.ISBN
            = NEW.ISBN
            ) -1 >=0 then
        update collectionofbook set TotalNum = TotalNum-1 where CollectionOfBook.ISBN
        = NEW.ISBN;
        end if;
    end;

create  trigger ReturnBook before insert on returnofbook
    for each row
    begin
        update collectionofbook set TotalNum = TotalNum+1 where CollectionOfBook.ISBN
        = NEW.ISBN;
    end;
