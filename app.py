import gradio as gr
import csv
def userinput(pos,flw,flg,bl,pic,lin,cl,cz,ni,erl,erc,It,hc,pr,fo,cs,pi):
    #insert trained model here
    # List that we want to add as a new row
    if (pic==['PIC']):
      pic1=1
    else :
      pic1=0
    if (lin==['Link']):
      lin1=1
    else :
      lin1=0
    List = [pos,flw,flg,bl,pic1,lin1,cl,cz,ni,erl,erc,It,hc,pr,fo,cs,pi]
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(r'/content/insert_data.csv', 'a') as f_object:

        # Pass this file object to csv.writer()
        # and get a writer object
        writer = csv.writer(f_object)

        # Pass the list as an argument into
        # the writerow()
        writer.writerow(List)

    output_str = "Hello"
    return output_str
interface=gr.Interface(
    fn = userinput,
    title = "Fake Profile Detection using Neural Netwroks",
    inputs = [
              gr.Number(label="No. of posts : "),
              gr.Number(label="Followers : "),
              gr.Number(label="Following : "),
              gr.Number(label="Bio length : "),
              #gr.inputs.Checkbox(label="Pic"),
              gr.CheckboxGroup(["PIC"], label="Profile Pic is avainlabel or not?"),
              #gr.inputs.Checkbox(label="Link"),
              gr.CheckboxGroup(["Link"], label="Any external link is available or not?"),
              gr.Number(label="Caption Length : "),
              #gr.Number(label="Caption zero : "),
              gr.Slider(0,1,float,label="Caption zero : "),
              #gr.Number(label="Non image percentage : "),
              gr.Slider(0,1,float,label="Non image percentage : "),
              gr.Number(label="Engagement rate (Like) : "),
              gr.Number(label="Engagement rate (Comm.) : "),
              #gr.Number(label="Location Tag % : "),
              gr.Slider(0,1,float,label="Location Tag % : "),
              gr.Number(label="Average Hashtag Count : "),
              #gr.Number(label="Promotional Keyword : "),
              gr.Slider(0,1,float,label="Promotional Keyword : "),
              gr.Number(label="Followers Keyword : "),
              #gr.Number(label="Cosine Similarity : "),
              gr.Slider(0,1,float,label="Cosine Similarity : "),
              gr.Number(label="Post Interval : "),
              ],
    outputs = ['text'],
    theme=gr.themes.Soft()
)
interface.launch()
