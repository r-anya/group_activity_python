"Automated Persistent Data Logging and Retrieval System Using File I/O Architecture"
import datetime

# Configuration of the permanent text storage block
STORAGE_FILE = "system_data_log.txt"

print("========================================")
print("⚙️ AUTOMATED DATA LOGGING INTERFACE")
print("========================================\n")
print("[1] Execute Log Entry Operation (Write Data)")
print("[2] Execute Log Retrieval Operation (Read Data)")
user_action = input("\nSelect system command (1 or 2): ").strip()

# --- MODULE 1: FILE OUTPUT (Data Streaming to Storage) ---
if user_action == "1":
    payload_data = input("\nEnter data packet payload to record:\n> ")
    
    # Generate precise execution timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open file in append ('a') mode to prevent overwriting historical records
    with open(STORAGE_FILE, "a") as file_stream:
        file_stream.write(f"TIMESTAMP: {current_time}\n")
        file_stream.write(f"PAYLOAD:   {payload_data}\n")
        file_stream.write("-" * 45 + "\n")
        
    print("\n✅ SUCCESS: Data packet successfully committed to non-volatile storage.")

# --- MODULE 2: FILE INPUT (Data Streaming from Storage) ---
elif user_action == "2":
    print("\n--- 📖 EXECUTING STORAGE READ BUFFER ---")
    try:
        # Open file in read ('r') mode to pull data into volatile memory
        with open(STORAGE_FILE, "r") as file_stream:
            retrieved_content = file_stream.read()
            
            # Check if the data stream contains any elements
            if not retrieved_content.strip():
                print("LOG STATUS: Target storage file is empty. No records found.")
            else:
                print(retrieved_content)
                
    except FileNotFoundError:
        # Runtime exception tracking for uninitialized storage targets
        print("⚠️ RUNTIME EXCEPTION: Target file not found. Initialize by generating a record.")

else:
    print("❌ ERROR: Invalid command sequence entered. Operation terminated.")
