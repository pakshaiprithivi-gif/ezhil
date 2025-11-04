import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load cloud cost data from CSV."""
    try:
        data = pd.read_csv(file_path)
        print("✅ Data loaded successfully!")
        return data
    except Exception as e:
        print("❌ Error loading file:", e)
        return None

def generate_summary(data):
    """Generate total and per-provider summaries."""
    print("\n--- Cloud Cost Summary ---")
    total_cost = data["Cost"].sum()
    print(f"Total Cloud Spend: ${total_cost:.2f}")

    provider_summary = data.groupby("Provider")["Cost"].sum()
    print("\nCost by Provider:")
    print(provider_summary)

    return total_cost, provider_summary

def visualize_costs(data):
    """Generate charts for visualization."""
    # Pie chart by Provider
    provider_summary = data.groupby("Provider")["Cost"].sum()
    provider_summary.plot(kind='pie', autopct='%1.1f%%', figsize=(6,6), title='Cloud Cost Distribution by Provider')
    plt.ylabel('')
    plt.tight_layout()
    plt.savefig("provider_cost_pie.png")
    plt.show()

    # Bar chart by Service
    plt.figure(figsize=(8,5))
    plt.bar(data["Service"], data["Cost"], color='skyblue')
    plt.title("Cost by Cloud Service")
    plt.xlabel("Service")
    plt.ylabel("Cost ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("service_cost_bar.png")
    plt.show()

def export_report(data, total_cost, provider_summary):
    """Save summary report to file."""
    with open("cloud_cost_report.txt", "w") as f:
        f.write("CLOUD COST VISUALIZER REPORT\n")
        f.write("=============================\n\n")
        f.write(f"Total Cloud Spend: ${total_cost:.2f}\n\n")
        f.write("Cost by Provider:\n")
        f.write(str(provider_summary))
    print("\n📁 Report saved as 'cloud_cost_report.txt'")

if __name__ == "__main__":
    data = load_data("sample_data.csv")
    if data is not None:
        total_cost, provider_summary = generate_summary(data)
        visualize_costs(data)
        export_report(data, total_cost, provider_summary)
