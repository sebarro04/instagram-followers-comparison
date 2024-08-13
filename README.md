# Instagram Followers Comparison

This is a simple program to get the accounts that you follow, but they don't follow back.

## How To Get The Necessary Files

1. **Open Instagram in your device (mobile).**
2. **Go to `Settings and activity`.**
3. **Go to `Your activity`.**
4. **Select `Download your information`.**
5. **Select `Download or transfer information`.**
6. **Select `Some of your information`.**
7. **In `Connections` select `Followers and following` then click `Next`.**
8. **Select `Download to device` then click `Next`.**
9. **In `Date range` select `All time`.**
10. **In `Format` select `JSON`.**
11. **Click `Create files`.**
12. **An email with a link to download the data will be sent to your email.**
13. **Download the data.**

## How To Use The Program

1. **Clone the repo to your machine.**
2. **Paste the files `connections/followers_and_following/followers_1.json` and `connections/followers_and_following/following.json` inside the repo.**
3. **Open the repo in a command line.**
4. **Go to the directory `src`.**
5. **Execute the program:**

```bash
python followers_comparison.py path-to-following-file path-to-followers-file
```