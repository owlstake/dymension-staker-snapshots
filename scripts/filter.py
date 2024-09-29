import csv

# Đặt giá trị ngưỡng cho "delegated dym" (có thể thay đổi)
threshold = 100

# Đọc file CSV, lọc các dòng có giá trị "delegated dym" nhỏ hơn threshold, và ghi vào file mới
def filter_and_save_delegated_dym(input_file_path, output_file_path, threshold):
    with open(input_file_path, mode='r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        
        # Mở file để ghi các dòng thỏa mãn điều kiện
        with open(output_file_path, mode='w', newline='') as csvoutfile:
            fieldnames = csvreader.fieldnames  # Lấy tên các cột từ file gốc
            csvwriter = csv.DictWriter(csvoutfile, fieldnames=fieldnames)
            
            # Ghi tiêu đề (header) vào file mới
            csvwriter.writeheader()
            
            # Lọc các dòng và ghi những dòng đạt điều kiện vào file mới
            for row in csvreader:
                delegated_dym = float(row['delegated dym'])
                if delegated_dym < threshold:
                    csvwriter.writerow(row)

# Đường dẫn đến file CSV gốc và file CSV đầu ra
input_file_path = 'delegators.csv'
output_file_path = 'filtered_delegators.csv'

# Gọi hàm để lọc và ghi kết quả vào file mới
filter_and_save_delegated_dym(input_file_path, output_file_path, threshold)
