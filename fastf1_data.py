import fastf1 
import pandas as pd

# Ensure caching is enabled (add this near the top of your file if not already there)
fastf1.Cache.enable_cache()

def get_practice_session_results(year, gp_round):
    """
    Retrieves and returns results for FP1, FP2, and FP3 for a specific F1 event.
    Args:
        year (int): The year of the F1 season.
        gp_round (int or str): The round number of the Grand Prix or event name (e.g., 'Monaco').
    Returns:
        dict: A dictionary containing DataFrames for FP1, FP2, and FP3 results,
              or None if an error occurs or no data is found.
    """
    practice_results = {}
    session_types = ['FP1', 'FP2', 'FP3']

    print(f"\n--- Retrieving Practice Session Data for {year} Round {gp_round} ---")

    for session_type in session_types:
        #Looking for all the seesion data 
        try : 
            session = fastf1.get_session(year, gp_round, session_type)
            print(f"Loading data for {year} Round {gp_round} ({session_type})...")
            session.load(telemetry=False, weather=False) # No need for telemetry/weather for basic results

            if not session.results.empty:
                # Select common and useful columns for practice results
                display_columns = ['Abbreviation', 'TeamName', 'Time', 'LapTime', 'Compound', 'TyreLife', 'Status']
                available_columns = [col for col in display_columns if col in session.results.columns]
                practice_results[session_type] = session.results[available_columns]
                print(f"{session_type} data loaded successfully.")
            else:
                print(f"No results found for {session_type}.")
                practice_results[session_type] = pd.DataFrame() # Add empty DataFrame if no results
        except Exception as e:
            print(f"An error occurred while getting {session_type} data: {e}")
            practice_results[session_type] = pd.DataFrame() # Add empty DataFrame on error
            # Continue to try other sessions even if one fails

    if not any(not df.empty for df in practice_results.values()):
        print(f"No practice session data found for {year} Round {gp_round}.")
        return None

    return practice_results
