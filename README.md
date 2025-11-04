
## 🌀 **Cloud Cost Visualizer Report Structure**

### 📘 Overview

The **Cloud Cost Visualizer Report Structure** project helps users analyze and visualize cloud infrastructure expenses across major providers such as **AWS**, **Azure**, and **GCP**.
It loads cost data from a CSV file, computes summaries, and generates easy-to-understand visual reports and text summaries for better cost management.

---

### 🚀 Features

* 📂 Load and process cloud cost data from a CSV file
* 💰 Compute total and per-provider cost summaries
* 📊 Generate **bar** and **pie** charts using `matplotlib`
* 🧾 Export a summary report (`cloud_cost_report.txt`)
* 🖼️ Save cost distribution images for documentation or reports

---

### 🛠️ Technologies Used

* **Python 3**
* **Pandas** — for data processing
* **Matplotlib** — for data visualization

---

### 📦 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Cloud-Cost-Visualizer.git
   ```
2. Navigate to the folder:

   ```bash
   cd Cloud-Cost-Visualizer
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### ▶️ How to Run

Run the project using:

```bash
python cloud_cost_visualizer.py
```

---

### 📊 Sample Data Format (`sample_data.csv`)

```csv
Provider,Service,Cost
AWS,EC2,120.50
AWS,S3,45.30
AWS,Lambda,10.75
Azure,VM,98.20
Azure,BlobStorage,55.10
GCP,ComputeEngine,110.60
GCP,CloudStorage,60.40
```

---

### 📈 Example Output

**Console Summary:**

```
--- Cloud Cost Summary ---
Total Cloud Spend: $500.85

Cost by Provider:
Provider
AWS      176.55
Azure    153.30
GCP      171.00
Name: Cost, dtype: float64
```

**Generated Files:**

* `provider_cost_pie.png` → Cost distribution by provider
* `service_cost_bar.png` → Cost per service
* `cloud_cost_report.txt` → Text-based summary report

---

### 🧩 Future Enhancements

* Integrate with **AWS Cost Explorer**, **Azure Billing**, and **GCP Cloud Billing APIs**
* Include **date-based trend visualization**
* Export **interactive dashboards**
* Generate reports in **PDF** format

---

### 👩‍💻 Author

Faizhun Nisha A
Ezhil mozhil S
