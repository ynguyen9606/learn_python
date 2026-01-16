class Product():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        while True:
            if 0 < price <= 100:
                self.price = price
                break
            else:
                print("Gia khong hop le, vui long nhap lai!")
                price = float(input("Nhap lai gia san pham: "))
        
        self.list_rate = []

    def viewInfo(self):
        print(f"ten san pham: {self.name}")
        print(f"gia san pham: {self.price}")
        print(f"mo ta san pham: {self.description}")

    def averageRate(self):
        if len(self.list_rate) == 0:
            return 0 
        return sum(self.list_rate) / len(self.list_rate)

class Shop:
    def __init__(self):
        self.Product_List = []
    
    def addProduct(self):
        print("\n=== THEM SAN PHAM MOI ===")
        name = input("nhap ten san pham: ")
        description = input("nhap mo ta san pham: ")
        price = float(input("nhap gia san pham: "))

        product = Product(name, description, price)

        n = int(input("nhap so luong danh gia: "))
        for i in range(n):
            rate = int(input(f" danh gia thu {i + 1} la (1-5): "))
            if 1 <= rate <= 5:
                product.list_rate.append(rate)

        self.Product_List.append(product)
        print("them thong tin san pham thanh cong")

    def removeProduct(self):
        name_remove = input("nhap ten san pham can xoa: ")
        for product_name in self.Product_List:
            if product_name.name == name_remove:
                self.Product_List.remove(product_name)
                print("da xoa san pham")
                return 
        print("khong tim thay san pham can xoa ! ")
    
    def iterateProductList(self):
        if not self.Product_List:
            print("danh sach san pham rong !")
            return
        
        for product in self.Product_List:
            product.viewInfo()
            print(f"trung binh cong danh gia san pham la: {product.averageRate():.2f}")
            print("-" * 10)

    def searchProduct(self):
        min_price = float(input("nhap gia san pham thap nhat: "))
        max_price = float(input("nhap gia san pham cao nhat: "))

        for product in self.Product_List:
            if min_price <= product.price <= max_price:
                product.viewInfo()
                print("-" * 10)

    def sortProduct(self):
        self.Product_List.sort(key=lambda p: p.price)
        print("san pham sap xep theo gia !")

def main():
    shop = Shop()

    while True:
        print("\nPRODUCT MANAGEMENT SYSTEM")
        print("1. Add new product")
        print("2. Remove product")
        print("3. Iterate product list")
        print("4. Search product")
        print("5. Sort product by price")
        print("6. Exit")

        choice = input("chon chuc nang: ")

        if choice == "1":
            shop.addProduct()
        elif choice == "2":
            shop.removeProduct()
        elif choice == "3":
            shop.iterateProductList()
        elif choice == "4":
            shop.searchProduct()
        elif choice == "5":
            shop.sortProduct()
        elif choice == "6":
            print("thoat chuong trinh.")
            break
        else:
            print("lua hcon khong hop le!")


if __name__ == "__main__":
    main()

