# 🔧 Troubleshooting Guide

**Common issues and solutions for Interior Scene Generator.**

---

## ❓ "I can't find Scripting tab in Blender"

**Solution:**
1. Look at the very top of Blender window
2. Small tabs: Layout, Modeling, Sculpting, **Scripting**
3. If missing: Window → Reset Layout
4. Or press F11 to reset workspace

---

## ❓ "Script doesn't work / Error message"

**Solutions:**
1. **Check Blender version:** Must be 3.0 or newer
   - Help → About Blender
   - Update if needed: blender.org/download/

2. **Check console output:**
   - Bottom of Blender window shows errors
   - Read error message carefully

3. **Re-download script:**
   - Delete old file
   - Download fresh copy from web interface

4. **Check Python syntax:**
   - Script should be exactly as provided
   - No modifications needed

---

## ❓ "Render is too dark or too bright"

**Solutions:**
1. **Adjust light energy:**
   - Select lights in scene (right panel)
   - Change "Energy" value (try 50-200)

2. **Adjust render settings:**
   - Render Properties → Light Paths
   - Increase "Max Bounces" (try 12-16)

3. **Adjust world strength:**
   - Shading → World
   - Adjust "Strength" value

---

## ❓ "Render takes too long"

**Solutions:**
1. **Normal time:** 1-5 minutes (depends on PC)
2. **Faster test render:**
   - Render Properties → Resolution
   - Set to 50% (960x540px)
3. **Use GPU:**
   - Render Properties → Device
   - Select "GPU Compute" (if available)

---

## ❓ "Materials don't look right"

**Solutions:**
1. **Check material assignment:**
   - Select object
   - Material Properties → Check material is assigned
2. **Adjust material:**
   - Shading workspace
   - Select material → Adjust values
3. **Re-run script:**
   - Script creates materials correctly
   - If modified, re-run script

---

## ❓ "Camera angle is wrong"

**Solutions:**
1. **Select camera:**
   - Right-click camera in scene
2. **Move camera:**
   - Press G (grab) → Move mouse → Click
3. **Rotate camera:**
   - Press R (rotate) → Move mouse → Click
4. **View from camera:**
   - Press Numpad 0 (or View → Camera)

---

## ❓ "Blender crashes / Freezes"

**Solutions:**
1. **Check system requirements:**
   - Minimum 4GB RAM
   - GPU recommended
2. **Reduce render settings:**
   - Lower samples (128 instead of 256)
   - Lower resolution (50%)
3. **Update Blender:**
   - Download latest version
   - blender.org/download/

---

## ❓ "Can't download script from web page"

**Solutions:**
1. **Check browser:**
   - Try different browser (Chrome, Firefox, Edge)
2. **Check popup blocker:**
   - Allow popups for this site
3. **Manual download:**
   - Right-click download button
   - "Save link as..."
4. **Alternative:**
   - Clone repository from GitHub
   - Get script from `src/create_interior_scene.py`

---

## 📞 Still Having Issues?

1. **Check Blender console** for error messages
2. **Update Blender** to latest version
3. **Re-download script** from web interface
4. **Open GitHub Issue** for support

---

**Status:** ✅ Comprehensive troubleshooting guide

