from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = 'data/profiles.json'

def load_profiles():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_profiles(profiles):
    with open(DATA_FILE, 'w') as f:
        json.dump(profiles, f, indent=4)

@app.route('/profiles', methods=['GET'])
def get_profiles():
    return jsonify(load_profiles())

@app.route('/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    profiles = load_profiles()
    for p in profiles:
        if p['id'] == profile_id:
            return jsonify(p)
    return jsonify({"error": "Profile not found"}), 404

@app.route('/profiles', methods=['POST'])
def add_profile():
    profiles = load_profiles()
    new_profile = request.get_json()
    new_profile['id'] = max([p['id'] for p in profiles] + [0]) + 1
    profiles.append(new_profile)
    save_profiles(profiles)
    return jsonify(new_profile), 201

@app.route('/profiles/<int:profile_id>', methods=['PUT'])
def update_profile(profile_id):
    profiles = load_profiles()
    updated = request.get_json()
    for i, p in enumerate(profiles):
        if p['id'] == profile_id:
            updated['id'] = profile_id
            profiles[i] = updated
            save_profiles(profiles)
            return jsonify(updated)
    return jsonify({"error": "Profile not found"}), 404

@app.route('/profiles/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    profiles = load_profiles()
    profiles = [p for p in profiles if p['id'] != profile_id]
    save_profiles(profiles)
    return jsonify({"message": f"Profile {profile_id} deleted."})

if __name__ == '__main__':
    app.run(port=5000)
